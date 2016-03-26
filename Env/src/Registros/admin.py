from django.contrib import admin
from .models import Victima,Registro,Actividad
from .forms import RegistroForm,VictimaForm

# Register your models here.
class VictimaAdmin(admin.ModelAdmin):
	list_display = ["id","__unicode__","edad","profesion","cui","sexo"]
	form = VictimaForm

class RegistroAdmin(admin.ModelAdmin):
	list_display = ["id","fecha","descripcion"]
	form = RegistroForm

admin.site.register(Victima,VictimaAdmin)
admin.site.register(Registro,RegistroAdmin)