from ..clients import OMDBClient


class TestOMDBClient:

    def test_returns_movie_rating_when_passing_valid_title(self, responses):
        responses.add(responses.GET, 'http://www.omdbapi.com', status=200,
                      json={'Title': 'Die Hard', 'imdbRating': '8.2'})

        rating = OMDBClient().get_rating_for_movie(title='Die Hard')

        assert rating == '8.2'
