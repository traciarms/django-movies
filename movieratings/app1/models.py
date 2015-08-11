import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


# Create your models here.
class Rater(models.Model):
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.IntegerField()
    zip_code = models.CharField(max_length=10)
    user = models.OneToOneField(User, null=True)

    def has_rated_movie(self, movie_id):
        rater = Rater.objects.get(pk=self.user.rater.id)
        ratings = rater.rating_set
        rated = len(ratings.filter(movie__id=movie_id)) > 0
        return rated

    def get_rating_list(self):
        return self.rating_set.all()

    def __str__(self):
        return 'id: {} gender: {} age: {} occupation: {} zip_code: {}'.\
            format(self.id, self.gender, self.age, self.occupation,
                   self.zip_code)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)

    def get_avg_rating(self):
        return self.rating_set.aggregate(Avg('ratings'))

    def get_user_list(self):
        return self.rating_set.all()

    def __str__(self):
        return 'title: {} genre: {}'.format(self.title, self.genre)


class Category(models.Model):
    category = models.CharField(max_length=150)
    movie = models.ManyToManyField(Movie)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    ratings = models.IntegerField(validators=[MinValueValidator(1),
                                              MaxValueValidator(5)])
    timestamp = models.IntegerField(default=0)
    new_stamp = models.DateTimeField()

    @property
    def was_published_recently(self):
        now = datetime.timezone.now()
        return now - datetime.timedelta(days=1) <= self.timestamp <= now

    def __str__(self):
        return 'rater: {} movie: {} ratings: {} timestamp: {}'.\
            format(self.rater, self.movie, self.ratings, self.timestamp)
