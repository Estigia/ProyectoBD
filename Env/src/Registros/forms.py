from django import forms
from .models import Registro,Victima

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Registro

		fields = ["fiscal",
					"descripcion",
					"movil",
					"no_expediente"					
			]

class VictimaForm(forms.ModelForm):
	class Meta:
		model = Victima

		fields = ["nombres",
					"apellidos",
					"edad",
					"muerto_herido",
					"profesion",
					"cui",
					"sexo",
				]
