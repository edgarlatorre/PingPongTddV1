from rest_framework import mixins, viewsets

from .models import Movie
from .serializers import MovieSerializer


class MoviesView(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
