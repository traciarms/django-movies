from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from app1.views import MovieList, MostRatings, DetailRater, DetailMovie, \
    AvgRating, CreateRating, DeleteRating, UpdateRating

urlpatterns = [
    # url(r'list_movies/', 'app1.views.list_movies', name='list_movies'),
    url(r'^list_movies/', MovieList.as_view(), name='list_movies'),
    url(r'^most_ratings/', MostRatings.as_view(), name='most_ratings'),

    url(r'^user/(?P<rater_id>[0-9]+)/', DetailRater.as_view(),
        name='detail_rater'),

    url(r'^detail_movie/(?P<movie_id>[0-9]+)/', DetailMovie.as_view(),
        name='detail_movie'),

    url(r'^create_rating/(?P<movie_id>[0-9]+)/',
        login_required(CreateRating.as_view()), name='create_rating'),

    url(r'^delete_rating/(?P<rating_id>[0-9]+)/',
        login_required(DeleteRating.as_view()), name='delete_rating'),

    url(r'^update_rating/(?P<rating_id>[0-9]+)/',
        login_required(UpdateRating.as_view()), name='update_rating'),

    url(r'^avg_rating/', AvgRating.as_view(),
        name='avg_rating'),

    # url(r'^create_rating/(?P<movie_id>[0-9]+)/', 'app1.views.create_rating',
    #     name='create_rating'),

    # url(r'avg_rating/(?P<select_category>[A-z]+)', 'app1.views.avg_rating',
    #     name='avg_rating'),
    # url(r'most_ratings/', 'app1.views.most_ratings', name='most_ratings'),
    # url(r'detail_movie/(?P<movie_id>[0-9]+)/', 'app1.views.detail_movie',
    #     name="detail_movie"),
    # url(r'^user/(?P<rater_id>[0-9]+)/', 'app1.views.detail_rater',
    #     name="detail_rater"),
    # url(r'^change_rating/(?P<rating_id>[0-9]+)/', 'app1.views.change_rating',
    #     name="change_rating"),
    # url(r'^delete_rating/(?P<rating_id>[0-9]+)/', 'app1.views.delete_rating',
    #     name="delete_rating"),

 ]