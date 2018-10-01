from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls))
]
