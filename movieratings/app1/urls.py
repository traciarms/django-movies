from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'app1.views.list_movies', name='list_movies'),
    url(r'avg_rating', 'app1.views.avg_rating', name='avg_rating'),
    url(r'(?P<movie_id>[0-9]+)/', 'app1.views.detail_movie',
        name="detail_movie"),
    url(r'(?P<rater_id>[0-9]+)/', 'app1.views.detail_rater',
        name="detail_rater"),

 ]