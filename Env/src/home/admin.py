from django.contrib import admin
from .forms import SignForm
from .models import Tipo_Usuario,Usuario

# Register your models here.

class Tipo_UsuarioAdmin(admin.ModelAdmin):
	list_display = ["id","__unicode__"]

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ["id","__unicode__","apellidos","Tipo_Usuario_id","ultima_conexion"]
	form = SignForm


admin.site.register(Tipo_Usuario,Tipo_UsuarioAdmin)
admin.site.register(Usuario,UsuarioAdmin)

