from rest_framework import serializers

from videoclub.flags import flag
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'price')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if flag.is_active('show_ratings'):
            representation['score'] = instance.score

        return representation
