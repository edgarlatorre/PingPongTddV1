from rest_framework import generics

from .models import Movie
from .serializers import MovieSerializer


class MoviesView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
