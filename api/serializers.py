from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id','tytul', 'opis', 'po_premierze')

class FilmMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('tytul',)