import pytest

from ..models import Movie


@pytest.mark.django_db
class TestMovie:

    def test_a_movie_is_created_when_passing_title_and_price(self):
        Movie.objects.create(title='Titanic', price='3.95')

        assert Movie.objects.count() == 1

    def test_a_movie_is_created_with_default_score_to_zero(self):
        Movie.objects.create(title='Titanic', price='3.95')

        movie = Movie.objects.first()
        assert movie.score == 0

