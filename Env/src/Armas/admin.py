from django.contrib import admin
from .forms import ArmaForm
from .models import Arma

class ArmaAdmin(admin.ModelAdmin):
	list_display = ["id","calibre","no_casquillos","marca","categoria","serial"]
	form = ArmaForm


admin.site.register(Arma, ArmaAdmin)