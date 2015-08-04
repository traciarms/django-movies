from django.contrib import admin

# Register your models here.
from .models import Rater
from .models import Movie
from .models import Rating

class RaterAdmin(admin.ModelAdmin):
    list_display = ('gender','age','occupation','zip_code')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','genre')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rater','movie','ratings','timestamp')


admin.site.register(Rater)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)