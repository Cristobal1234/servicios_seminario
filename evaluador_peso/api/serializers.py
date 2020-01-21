from rest_framework import serializers
from evaluador_peso import models as model_pesos

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model   = model_pesos.Persona
        fields  = "__all__"