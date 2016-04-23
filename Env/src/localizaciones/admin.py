from django.contrib import admin
from .forms import MunicipioForm,DepartamentoForm
from .models import Departamento,Municipio
# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ["id","departamento"]
	form = DepartamentoForm

class MunicipioAdmin(admin.ModelAdmin):
	list_display = ["id","municipio"]
	form = MunicipioForm

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
