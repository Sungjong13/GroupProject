from django.urls import path

from . import views

urlpatterns = [
    path('', views.map_window, name='map_window'),
]
