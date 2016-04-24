from django.contrib import admin
from .forms import ArmaForm
from .models import Arma

class ArmaAdmin(admin.ModelAdmin):
	list_display = ["id","calibre","marca","categoria","objeto"]
	form = ArmaForm


admin.site.register(Arma, ArmaAdmin)