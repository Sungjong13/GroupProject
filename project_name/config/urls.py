"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from config.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings
from users.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store_home/', views.home, name='store_home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('users/',include('users.urls')),
    
    path('payment/',include('payment.urls')),
   
    path("accounts/", include("allauth.urls")),
    path('map/', include('map.urls')),

    # test home
    path('', HomeView.as_view(), name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
