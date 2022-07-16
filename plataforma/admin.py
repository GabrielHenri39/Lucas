from django.contrib import admin
from .models import Paciente, DadosPaciente

# Register your models here.

admin.site.register(Paciente)
admin.site.register(DadosPaciente)