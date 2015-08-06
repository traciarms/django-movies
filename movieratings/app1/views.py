import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

# Create your views here.
from app1.forms import RatingForm
from app1.models import Movie, Rater

def list_movies(request):
    # get info you need
    movies = Movie.objects.all().order_by('title')
    # setup dictionary of variables that the template can use
    # render the request
    return render(request, 'app1/list_movies.html', {'movies': movies})


@login_required(login_url='/login')
def create_rating(request, movie_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie_id = movie_id
            rating.rater_id = request.user.rater.id
            rating.save()

            return HttpResponseRedirect(reverse('detail_movie', args=[movie_id]))
            #return render(request, 'app1/create_rating.html', {'form':form})

    else:
        form = RatingForm()
    return render(request, 'app1/create_rating.html', {'form':form, 'movie_id':movie_id})


def avg_rating(request):
    movies = Movie.objects.all()
    movie_ratings = []
    for movie in movies:
        rating = movie.get_avg_rating().get('ratings__avg')
        if rating != None:
            movie_ratings.append((movie, rating))

    movie_ratings = sorted(movie_ratings, key=lambda x: x[1], reverse=True)
    movie_ratings = movie_ratings[:20]

    return render(request, 'app1/avg_rating.html',
                  {'movie_ratings': movie_ratings})


def detail_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    avg_rating = movie.get_avg_rating().get('ratings__avg')
    user_list = movie.get_user_list()
    rated = request.user.rater.has_rated_movie(movie_id)

    return render(request, 'app1/detail_movie.html', {'movie': movie,
                                                      'avg_rating': avg_rating,
                                                      'user_list': user_list,
                                                      'rated': rated})

def detail_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings_list = rater.get_rating_list()

    return render(request, 'app1/detail_rater.html', {'rater': rater,
                                                      'ratings_list': ratings_list})