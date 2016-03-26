from django import forms
from .models import Municipio,Departamento,Localizacion

class LocalizacionForm(forms.ModelForm):
	class Meta:
		model = Localizacion
		fields = ["direccion","tipo"]

class MunicipioForm(forms.ModelForm):
	class Meta:
		model = Municipio
		fields = ["nombre"]

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = ["nombre"]