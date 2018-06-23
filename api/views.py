from django.shortcuts import render
from django.contrib.auth.models import User
from api.serializers import MovieRecordsSerializer
from rest_framework.response import Response
from rest_framework import viewsets
# from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from django.http import HttpResponse
from .models import MovieRecords, MovieGenres
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
import random, string, types
from rest_framework import generics
from django.core import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import json
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from django.views import generic


class MoviesViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    serializer_class = MovieRecordsSerializer

    def get_queryset(self):
        queryset = MovieRecords.objects.all()
        term = self.request.query_params.get('term', None)
        director = self.request.query_params.get('director', None)

        if term is not None:
            queryset = queryset.filter(name__icontains = term)

        if director is not None:
            queryset = queryset.filter(director__icontains = director)

        return queryset


class LoadDataView(APIView):
    permission_classes = (IsAdminUser, )

    def get(self, request, *args, **kw):
        condition = True
        data=None
        message=""

        if MovieGenres.objects.exists() or MovieRecords.objects.exists():
            condition = False
            message = "Records Already exists"

        if condition:
            message = "Records Added Successfully"
            with open('/home/deestar/projects/myimdb/api/imdb.json') as myfile:
                data = json.load(myfile)

            for movie in data:
                my_obj = MovieRecords.objects.get_or_create(
                    popularity = movie['99popularity'],
                    imdb_score=movie['imdb_score'],
                    director=movie['director'],
                    name=movie['name'],
                )

                for name in movie['genre']:
                    myg = MovieGenres.objects.get_or_create(name=name.strip())
                    my_obj[0].genre.add(myg[0])


        data = MovieRecords.objects.all().values()

        responseData = {
            'message': message,
            'data': data,
            'error': None
        }

        return Response(responseData, status=status.HTTP_200_OK)

class HomePageView(generic.TemplateView):
    template_name = 'index.html'