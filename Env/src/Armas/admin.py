from django.contrib import admin
from .forms import ArmaForm, Tipo_ArmaForm
from .models import Arma,Tipo_Arma

class Tipo_ArmaAdmin(admin.ModelAdmin):
	list_display = ["id","__unicode__"]
	form = Tipo_ArmaForm

class ArmaAdmin(admin.ModelAdmin):
	list_display = ["id","calibre","no_casquillos","marca","categoria","serial","Tipo_Arma_id"]
	form = ArmaForm

admin.site.register(Tipo_Arma, Tipo_ArmaAdmin)
admin.site.register(Arma, ArmaAdmin)