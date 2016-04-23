from django.contrib import admin
from .models import Registro,Actividad
from .forms import RegistroForm

# Register your models here.

class RegistroAdmin(admin.ModelAdmin):
	list_display = ["id","nombres","apellidos","edad","muerto",
					"profesion","cui","sexo","fiscal","fecha",
					"fecha_registro","descripcion","movil","no_expediente"]
	form = RegistroForm

class ActividadAdmin(admin.ModelAdmin):
	list_display = ["id","Registro_id","Usuario_id","actividad"]

admin.site.register(Registro,RegistroAdmin)
admin.site.register(Actividad,ActividadAdmin)





