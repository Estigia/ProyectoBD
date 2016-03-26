from django import forms
from .models import Arma
from .models import Tipo_Arma
class ArmaForm(forms.ModelForm):
	class Meta:
		model = Arma

		fields = ["calibre",
					"no_casquillos",
					"marca",
					"categoria",
					"serial",
					]	

class Tipo_ArmaForm(forms.ModelForm):
	class Meta:
		model = Tipo_Arma

		fields = ["objeto"

					]