from django import forms
from .models import Arma

class ArmaForm(forms.ModelForm):
	class Meta:
		model = Arma

		fields = ["categoria",
					"objeto",
					"calibre",
					"no_casquillos",
					"marca",					
					"serial"					
				]	



