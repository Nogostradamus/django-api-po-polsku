from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action

from api.serializers import UserSerializer
from .models import Film, Recenzja, Aktor
from .serializers import FilmSerializer, RecenzjaSerializer, AktorSerializer

class FilmySetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tytul', 'opis', 'rok')
    search_fields = ('tytul', 'opis')
    ordering_fields = '__all__'
    ordering = ('rok',)
    pagination_class = FilmySetPagination

    def get_queryset(self):
        # rok = self.request.query_params.get('rok', None)
        # id = self.request.query_params.get('id', None)
        #
        # if id:
        #     filmy = Film.objects.filter(id=id)
        # else:
        #     if rok:
        #         filmy = Film.objects.filter(rok=rok)
        #     else:
        #         filmy = Film.objects.all()
        filmy = Film.objects.all()
        return filmy

    # def list(self, request, *args, **kwargs):
    #     tytul = self.request.query_params.get('tytul', None)
    #
    #     #filmy = Film.objects.filter(tytul__exact=tytul)
    #     #filmy = Film.objects.filter(tytul__contains=tytul)
    #     filmy = Film.objects.filter(premiera__year="2000")
    #
    #     #queryset = self.get_queryset()
    #
    #     serializer = FilmSerializer(filmy, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        #if request.user.is_superuser:
        film = Film.objects.create(tytul=request.data['tytul'],
                               opis=request.data['opis'],
                               po_premierze=request.data['po_premierze'],
                                   rok=request.data['rok'])
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)
        #else:
        #    return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.tytul = request.data['tytul']
        film.opis = request.data['opis']
        film.po_premierze = request.data['po_premierze']
        film.rok = request.data['rok']
        film.save()

        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        film = self.get_object()
        film.delete()
        return Response('Film usuniety')

    @action(detail=True)
    def premiera(self, request, **kwargs):
        film = self.get_object()
        film.po_premierze = True
        film.save()

        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def premiera_wszystkie(self, request, **kwargs):
        filmy = Film.objects.all()
        filmy.update(po_premierze=request.data['po_premierze'])

        serializer = FilmSerializer(filmy, many=True)
        return Response(serializer.data)

class RecenzjeViewSet(viewsets.ModelViewSet):
    queryset = Recenzja.objects.all()
    serializer_class = RecenzjaSerializer

class AktorViewSet(viewsets.ModelViewSet):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer

    @action(detail=True, methods=['post'])
    def dolacz(self, request, **kwargs):
        aktor = self.get_object()
        film = Film.objects.get(id=request.data['film'])
        aktor.filmy.add(film)

        serializer = AktorSerializer(aktor, many=False)
        return Response(serializer.data)
