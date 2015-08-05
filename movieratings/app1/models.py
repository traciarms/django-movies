from django.db import models
from django.db.models import Avg

# Create your models here.

class Rater(models.Model):
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.IntegerField()
    zip_code = models.CharField(max_length=5)

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


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    ratings = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return 'rater: {} movie: {} ratings: {} timestamp: {}'.\
            format(self.rater, self.movie, self.ratings, self.timestamp)