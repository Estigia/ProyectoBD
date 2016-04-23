from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Registro

		fields = ["nombres",
					"apellidos",
					"edad",
					"muerto",
					"profesion",
					"cui",
					"sexo",
					"fiscal",
					"fecha",
					"descripcion",
					"movil",
					"no_expediente",
					"Localizacion_id",
					"Arma_id",							
			]

