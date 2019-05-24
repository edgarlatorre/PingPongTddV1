import pytest
from rest_framework import status


@pytest.mark.django_db
class TestGetMovies:

    def test_returns_movie_when_movie_exists(self, client, movie):
        response = client.get(f'/movies/{movie.id}')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'title': 'John Wick',
            'price': '10.00',
        }

    def test_returns_not_found_when_movie_does_not_exist(self, client):
        response = client.get('/movies/1')

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestListMovies:

    def test_returns_empty_list_when_no_movies_exist(self, client):
        response = client.get('/movies/')

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []
