from django.contrib import admin
from .models import Registro,Actividad
from .forms import RegistroForm

# Register your models here.

class RegistroAdmin(admin.ModelAdmin):
	list_display = ["id","nombres","apellidos","edad","muerto",
					"profesion","cui","sexo","fiscal","fecha",
					"fecha_registro","descripcion","movil","no_expediente"]
	form = RegistroForm

admin.site.register(Registro,RegistroAdmin)



