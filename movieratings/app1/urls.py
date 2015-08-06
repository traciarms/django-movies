from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', 'app1.views.list_movies', name='list_movies'),
    url(r'create_rating/(?P<movie_id>[0-9]+)/', 'app1.views.create_rating',
        name='create_rating'),
    url(r'avg_rating/', 'app1.views.avg_rating', name='avg_rating'),
    url(r'^(?P<movie_id>[0-9]+)/', 'app1.views.detail_movie',
        name="detail_movie"),
    url(r'^user/(?P<rater_id>[0-9]+)/', 'app1.views.detail_rater',
        name="detail_rater"),

    #url(r'load_data', 'app1.views.create_user', name='create_user'),

 ]