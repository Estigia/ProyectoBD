from django import forms
from .models import Arma
from django.contrib.admin import widgets

class ArmaForm(forms.ModelForm):
	class Meta:
		model = Arma

		fields = ["categoria",
					"objeto",
					"calibre",
					"marca",					
				]	

	def __init__(self, *args, **kwargs):
		super(ArmaForm, self).__init__(*args, **kwargs)

		self.fields['objeto'].widget = forms.TextInput(attrs={
			'placeholder' : 'Herramienta del acto'
			})

		self.fields['marca'].widget = forms.TextInput(attrs={
			'placeholder' : 'toto'
			})

