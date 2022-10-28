from django.urls import path
from users import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("account/", views.create_account, name="user_register"),
    path("check_email/", views.check_email, name="check_email"),
    path("check_nickname/", views.check_nickname, name="check_nickname"),
]
