from django.contrib.auth import get_user_model
from rest_framework import serializers, models
from .models import MovieRecords, MovieGenres

UserModel = get_user_model()


class GenreSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return '%s' % (value.name)

    class Meta:
        model = MovieGenres
        fields = ( 'name' ,)



class MovieRecordsSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)


    class Meta:
        model = MovieRecords
        fields = ('popularity','director', 'genre', 'imdb_score', 'genre', 'name', 'id')


    def __init__(self, *args, **kwargs):
        super(MovieRecordsSerializer, self).__init__(*args, **kwargs)
        user = self.context['request'].user
        if not user.is_superuser:
            self.fields.pop('id')


    def create(self, validated_data):
        genres_data = validated_data.pop('genre')
        movie_record = MovieRecords.objects.get_or_create(**validated_data)[0]

        for genre in genres_data:
            mg = MovieGenres.objects.get_or_create(**genre)[0]

            movie_record.genre.add(mg)

        return movie_record


    def update(self, movie_record, validated_data):
        genres_data = validated_data.pop('genre')
        movie_record.__dict__.update(**validated_data)

        movie_record.save()
        movie_record.genre.clear()

        for genre in genres_data:
            mg = MovieGenres.objects.get_or_create(**genre)[0]

            movie_record.genre.add(mg)

        return movie_record