from django import forms
from .models import Municipio,Departamento,Localizacion

class LocalizacionForm(forms.ModelForm):
	class Meta:
		model = Localizacion
		fields = ["direccion","especifico","Municipio_id"]

class MunicipioForm(forms.ModelForm):
	class Meta:
		model = Municipio
		fields = ["Departamento_id","municipio"]

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = ["departamento"]