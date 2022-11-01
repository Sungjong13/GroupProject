from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/detail/<int:pk>", views.post_detail, name="post_detail"),
]
