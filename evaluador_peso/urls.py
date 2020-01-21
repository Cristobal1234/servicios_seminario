"""imc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from evaluador_peso.api.viewsets import BuscarPersonaViewSet, RegistrarPersonaViewSet, CalcularIMC
from . import views

urlpatterns = [
    path('api/registrar/',RegistrarPersonaViewSet.as_view(),name="registrar"),
    re_path('^buscar/(?P<nombre>[-\w]+)/(?P<contrasena>[-\w]+)/',BuscarPersonaViewSet.as_view(),name="buscado"),
    re_path('^calcular/(?P<nombre>[-\w]+)/',CalcularIMC.as_view(),name="calcular"),
    path("calculador/<nombre>/<peso>/<estatura>",views.calculoIMC,name="reporte"),
]