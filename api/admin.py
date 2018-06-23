from django.contrib import admin

from django.contrib import admin
from .models import MovieRecords, MovieGenres

class MovieRecordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'imdb_score', 'popularity','director')

admin.site.register(MovieRecords, MovieRecordsAdmin)
admin.site.register(MovieGenres)