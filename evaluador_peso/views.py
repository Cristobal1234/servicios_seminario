from django.shortcuts import render
from django import views
from django.http import request, HttpResponse, JsonResponse
from evaluador_peso import models as model_peso


def calculoIMC(request,nombre,peso,estatura):
    if request.method == "GET":
        id  = request.GET.get("nombre")
        resultado = model_peso.Persona.objects.filter(nickname=nombre).values()
        if len(resultado)==0:
            return JsonResponse({"imc":"no esta registrado en la plataforma"})
        else:
            
            imc = float(peso)/(float(estatura)*float(estatura))
            return JsonResponse({"imc":imc})
    return HttpResponse({"hola":1})