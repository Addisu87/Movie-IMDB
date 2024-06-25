from django.contrib import admin
from core.movies.models import Movie, Rating, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Review)
