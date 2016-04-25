from django import forms
from .models import Registro
from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget

class RegistroForm(forms.ModelForm):

	class Meta:
		model = Registro

		widgets = {
            'fecha': DateTimeWidget(usel10n = True, bootstrap_version=3)
        }	

		fields = ["Arma",
					"no_casquillos",	
					"serial",				
					"nombres",
					"apellidos",
					"edad",
					"muerto",
					"profesion",
					"cui",
					"sexo",
					"ubicacion",
					"fiscal",
					"fecha",
					"descripcion",
					"movil",
					"no_expediente",
					"Municipio",
												
			]

	def __init__(self, *args, **kwargs):
		super(RegistroForm, self).__init__(*args, **kwargs)

		self.fields['ubicacion'].widget = forms.Textarea(attrs={
			'placeholder' : 'Escriba direccion exacta o una referencia a la misma.'
			})

		self.fields['descripcion'].widget = forms.Textarea(attrs={
			'placeholder' : 'Nota de la parte policial.'
			})

