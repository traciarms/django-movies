from django.shortcuts import render
from django.template import loader

# Create your views here.
from app1.models import Movie, Rater

def list_movies(request):
    # get info you need
    movies = Movie.objects.all().order_by('title')
    # setup dictionary of variables that the template can use
    # render the request
    return render(request, 'app1/list_movies.html', {'movies': movies})

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

    return render(request, 'app1/detail_movie.html', {'movie': movie,
                                                      'avg_rating': avg_rating,
                                                      'user_list': user_list})

def detail_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings_list = rater.get_rating_list()

    return render(request, 'app1/detail_rater.html', {'rater': rater,
                                                      'ratings_list': ratings_list})