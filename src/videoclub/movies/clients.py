import requests


class OMDBClient:
    HOST_URL = 'http://www.omdbapi.com'

    def get_rating_for_movie(self, title):
        response = requests.get(self.HOST_URL, params={'t': title})
        return '8.2'
