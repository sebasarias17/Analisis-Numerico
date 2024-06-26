"""
URL configuration for analisis_numerico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .metodos.views import *
from analisis_numerico.metodos.views import interpolate_vandermonde, download_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cap1/', cap1, name='cap1'),
    path('cap2/', cap2, name='cap2'),
    path('cap3/', cap3, name='cap3'),
    path('cap4/', cap4, name='cap4'),
    path('vandermonde/', interpolate_vandermonde, name = 'vandermonde'),
    path('download/<str:filename>/', download_file, name='download_file'), 
    path('newtoninterpolante/', interpolate_newton, name='newton'),
    path('download/<str:filename>/', download_file, name='download_file'),
    #path('newton_raphson/', newton_raphson_view, name='newton_raphson'),
]
