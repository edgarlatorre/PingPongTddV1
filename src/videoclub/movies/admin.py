from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from videoclub.movies.models import Movie


@register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'price', 'score',)
    list_filter = ('genre',)

