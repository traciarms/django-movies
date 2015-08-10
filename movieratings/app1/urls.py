from django.conf.urls import url, include

urlpatterns = [
    url(r'list_movies/', 'app1.views.list_movies', name='list_movies'),
    url(r'create_rating/(?P<movie_id>[0-9]+)/', 'app1.views.create_rating',
        name='create_rating'),
    url(r'avg_rating/', 'app1.views.avg_rating', name='avg_rating'),
    url(r'most_ratings/', 'app1.views.most_ratings', name='most_ratings'),
    url(r'detail_movie/(?P<movie_id>[0-9]+)/', 'app1.views.detail_movie',
        name="detail_movie"),
    url(r'^user/(?P<rater_id>[0-9]+)/', 'app1.views.detail_rater',
        name="detail_rater"),
    url(r'^change_rating/(?P<rating_id>[0-9]+)/', 'app1.views.change_rating',
        name="change_rating"),
    url(r'^delete_rating/(?P<rating_id>[0-9]+)/', 'app1.views.delete_rating',
        name="delete_rating"),

    #url(r'load_data', 'app1.views.create_user', name='create_user'),
#(?P<user.rater.id>[0-9]+)/
 ]