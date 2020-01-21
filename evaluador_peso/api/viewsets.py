from rest_framework import generics, viewsets
from evaluador_peso import models as models_pesos
from . import serializers


class RegistrarPersonaViewSet(generics.CreateAPIView, generics.ListAPIView):
    serializer_class       = serializers.PersonaSerializer
    queryset               = models_pesos.Persona.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
    

class BuscarPersonaViewSet(generics.ListAPIView):
    serializer_class = serializers.PersonaSerializer

    def get_queryset(self):
        nombre2     = self.kwargs.get("nombre")
        contrasena2  = self.kwargs.get("contrasena")
        return models_pesos.Persona.objects.filter(nombre=nombre2,password=contrasena2)
        

class CalcularIMC(generics.ListAPIView):
    serializer_class = serializers.PersonaSerializer

    def get_queryset(self):
        nombre2     = self.kwargs.get("nombre")
        input("hola")
        return {"imc":13}