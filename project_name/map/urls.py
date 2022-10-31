from django.urls import path

from . import views

urlpatterns = [
    path('', views.map_window, name='map_window'),
    path('map_update/', views.map_update, name='map_update'),
]
