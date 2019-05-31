import pytest
from django.contrib.admin import AdminSite

from videoclub.movies.admin import MovieAdmin
from videoclub.movies.models import Movie


class TestMovieAdmin:

    @pytest.fixture
    def admin_site(self):
        return AdminSite()

    @pytest.fixture
    def movie_admin(self, admin_site):
        return MovieAdmin(Movie, admin_site)

    def test_fields_are_set(self, movie_admin):
        assert movie_admin.fields == ('title', 'price', 'score',)

    def test_list_filter_are_set(self, movie_admin):
        assert movie_admin.list_filter == ('genre',)
