import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from app1.forms import RatingForm
from app1.models import Movie, Rater, Rating


def list_movies(request):
    # get info you need
    movies = Movie.objects.all().order_by('title')
    # setup dictionary of variables that the template can use
    # render the request
    return render(request, 'app1/list_movies.html', {'movies': movies})


@login_required(login_url='/login')
def change_rating(request, rating_id):

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = Rating.objects.get(pk=rating_id)
            form_rating = form.save(commit=False)
            rating.movie_id = rating.movie.id
            rating.rater_id = request.user.rater.id
            rating.new_stamp = datetime.datetime.now()
            rating.ratings = form_rating.ratings
            rating.save()

            return HttpResponseRedirect(reverse('account_profile'))

    else:
        form = RatingForm()
    return render(request, 'app1/change_rating.html', {'form': form,
                                                       'rating_id': rating_id})


@login_required(login_url='/login')
def delete_rating(request, rating_id):

    rating = Rating.objects.get(pk=rating_id)

    if request.method == 'POST':
        if "delete" in request.POST:
            rating.delete()

        return HttpResponseRedirect(reverse('account_profile'))
    else:
        form = Form()

    return render(request, 'app1/delete_rating.html', {'form': form,
                                                       'rating_id': rating_id})


@login_required(login_url='/login')
def account_profile(request):
    rater = Rater.objects.get(pk=request.user.rater.id)
    ratings_list = rater.get_rating_list()
    return render(request, 'app1/account_profile.html',
                  {'ratings_list': ratings_list})


@login_required(login_url='/login')
def create_rating(request, movie_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie_id = movie_id
            rating.rater_id = request.user.rater.id
            rating.new_stamp = datetime.datetime.now()
            rating.save()

            return HttpResponseRedirect(reverse('detail_movie',
                                                args=[movie_id]))

    else:
        form = RatingForm()
    return render(request, 'app1/create_rating.html', {'form': form,
                                                       'movie_id': movie_id})


def avg_rating(request):
    movies = Movie.objects.all()
    movie_ratings = []
    for movie in movies:
        rater_list = movie.get_user_list()
        rating = movie.get_avg_rating().get('ratings__avg')
        if rating is not None:
            movie_ratings.append((movie, rating, rater_list))

    movie_ratings = sorted(movie_ratings, key=lambda x: x[1], reverse=True)
    movie_ratings = movie_ratings[:20]

    return render(request, 'app1/avg_rating.html',
                  {'movie_ratings': movie_ratings})

    # movie_list = Movie.objects.all()
    # avg_rating = movie_list.annotate(
    #     overall=Avg('ratings__avg')).order_by('-overall')[:20]
    #
    # return render(request, 'app1/avg_rating.html',
    #               {"movie_list": movie_list, "avg_rating": avg_rating})


def most_ratings(request):
    movies = Movie.objects.all()
    movie_ratings = []
    for movie in movies:
        rater_list = movie.get_user_list()
        num_rated = len(rater_list)
        print('the number of ratings is {}:'.format(num_rated))
        if rater_list is not None:
            movie_ratings.append((movie, rater_list, num_rated))

    movie_ratings = sorted(movie_ratings, key=lambda x: len(x[1]), reverse=True)
    movie_ratings = movie_ratings[:20]

    return render(request, 'app1/most_ratings.html',
                  {'movie_ratings': movie_ratings})


def detail_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    avg_rating = movie.get_avg_rating().get('ratings__avg')
    user_list = movie.get_user_list()
    if request.user.is_authenticated():
        rated = request.user.rater.has_rated_movie(movie_id)
    else:
        rated = False

    return render(request, 'app1/detail_movie.html', {'movie': movie,
                                                      'avg_rating': avg_rating,
                                                      'user_list': user_list,
                                                      'rated': rated})

def detail_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings_list = rater.get_rating_list()

    return render(request, 'app1/detail_rater.html', {'rater': rater,
                                                      'ratings_list': ratings_list})