from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name="home")
]

handler404 = views.http404
handler500 = views.http500

