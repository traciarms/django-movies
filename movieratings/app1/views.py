import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Avg, Count
from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView
from app1.forms import RatingForm
from app1.models import Movie, Rater, Rating, Category


class MovieList(ListView):
    model = Movie
    template_name = "app1/list_movies.html"
    queryset = Movie.objects.all().order_by('title')
    paginate_by = 20


class MostRatings(ListView):
    model = Movie
    template_name = "app1/most_ratings.html"
    queryset = Movie.objects.exclude(rating=None).annotate(
        count=Count('rating__ratings')).order_by('-count')[:20]
    paginate_by = 10


# class MovieDetail(DetailView):
#     model = Movie
#     template_name = "app1/detail_movie.html"
#     pk_url_kwarg = 'movie_id'
#     avg_rating = movie.get_avg_rating().get('ratings__avg')
#     user_list = movie.get_user_list()
#     if request.user.is_authenticated():
#         rated = request.user.rater.has_rated_movie(movie_id)
#     else:
#         rated = False
#     paginate_by = 10
#
#     def get_context_data(self, **kwargs):
#         context = super(MovieList, self).get_context_data(**kwargs)
#         context['rated'] =
#         return context

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
# class AvgRating(ListView):
#     model = Movie
#     template_name = "app1/avg_rating.html"
#     # pk_url_kwarg = 'select_category'
#     queryset = Movie.objects.exclude(rating=None)
#     # if select_category != 'None':
#     #     queryset = queryset.filter(category__category__icontains=select_category)
#     queryset = queryset.annotate(
#         average=Avg('rating__ratings')).order_by('-average')[:20]
#     paginate_by = 10


def avg_rating(request, select_category=None):
    category_list = Category.objects.all()
    movie_list = Movie.objects.exclude(rating=None)
    if select_category != 'None':
        movie_list = movie_list.filter(category__category__icontains=select_category)
    avg_rating = movie_list.annotate(
        average=Avg('rating__ratings')).order_by('-average')[:20]

    return render(request, 'app1/avg_rating.html',
                  {'avg_rating': avg_rating,
                   'category_list': category_list,
                   'select_category': select_category})


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


def detail_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings_list = rater.get_rating_list()

    return render(request, 'app1/detail_rater.html',
                  {'rater': rater, 'ratings_list': ratings_list})
