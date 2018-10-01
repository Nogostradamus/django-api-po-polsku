from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film, ExtraInfo, Recenzja, Aktor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')

class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ('czas_trwania', 'rodzaj')

class RecenzjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recenzja
        fields = ('opis', 'gwiazdki')


class FilmSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    recenzje = RecenzjaSerializer(many=True)

    class Meta:
        model = Film
        fields = ('id','tytul', 'opis', 'po_premierze',
                  'premiera', 'rok', 'imdb_rating',
                  'extra_info', 'recenzje')

class FilmMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id','tytul')


class AktorSerializer(serializers.ModelSerializer):
    filmy = FilmMiniSerializer(many=True)
    class Meta:
        model = Aktor
        fields = ('imie', 'nazwisko', 'filmy')




