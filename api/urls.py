from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'filmy', views.FilmViewSet, base_name="film")
router.register(r'recenzje', views.RecenzjeViewSet, base_name="recenzje")
router.register(r'aktorzy', views.AktorViewSet, base_name="aktorzy")

urlpatterns = [
    url(r'^', include(router.urls))
]
