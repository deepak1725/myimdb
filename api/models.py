from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class MovieGenres(models.Model):
    name = models.CharField("Movie Genree", max_length=255)

    def __str__(self):
        return self.name



class MovieRecords(models.Model):
    popularity = models.DecimalField(decimal_places=1 , max_digits=4, validators=[MinValueValidator(0), MaxValueValidator(100)])
    director = models.CharField(max_length=255)
    genre = models.ManyToManyField(MovieGenres)
    imdb_score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)],)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


