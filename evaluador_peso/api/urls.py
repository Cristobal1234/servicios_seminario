from django.conf.urls import url 
from .viewsets import *
from django.urls import path, re_path



urlpatterns = [
    path('registrar/', RegistrarPersonaViewSet.as_view(), name='registrar'),
    re_path(r'^buscar/(?P<nombre>.+)/',BuscarPersonaViewSet.as_view(),name="buscar"),
]