from django.contrib import admin
from .forms import LocalizacionForm,MunicipioForm,DepartamentoForm
from .models import Departamento,Municipio,Localizacion
# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ["id","departamento"]
	form = DepartamentoForm

class MunicipioAdmin(admin.ModelAdmin):
	list_display = ["id","municipio"]
	form = MunicipioForm

class LocalizacionAdmin(admin.ModelAdmin):
	list_display = ["direccion","especifico", "Municipio_id"]
	form = LocalizacionForm

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Localizacion, LocalizacionAdmin)
