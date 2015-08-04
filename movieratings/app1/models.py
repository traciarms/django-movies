from django.db import models

# Create your models here.
class Rater(models.Model):
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=5)

    def ave_rating(self):
        return self.ave_rating

    def top_movies(self):
        return self.top_movies

    def __unicode__(self):
        return self.id

class Movie(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)

    # def ave_rating(self):
    #     return self.ave_rating
    #
    # def top_movies(self):
    #     return self.top_movies

    def __unicode__(self):
        return self.title


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    ratings = models.FloatField()
    timestamp = models.DateTimeField()