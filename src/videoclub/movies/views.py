from rest_framework import viewsets

from .models import Movie
from .serializers import MovieSerializer


class MoviesView(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
