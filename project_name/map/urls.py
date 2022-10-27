from django.urls import path

from . import views

urlpatterns = [
    path('', views.map_window, name='map_window'),
    path('ajax_test/', views.ajax_test, name='ajax_test'),
]
