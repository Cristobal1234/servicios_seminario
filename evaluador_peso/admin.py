from django.contrib import admin
from . import models as model_imc

class PersonaAdmin(admin.ModelAdmin):
    list_display = ("peso","nombre","estatura")



admin.site.register(model_imc.Persona, PersonaAdmin)