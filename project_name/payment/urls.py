from django.urls import path
from . import views

app_name = "kakaopay"

urlpatterns = [
    path('', views.payment, name="payment"),
    path('approval/', views.approval, name="approval"),    
    path('approval_success/', views.approval_success, name="approval_success"),
    
]