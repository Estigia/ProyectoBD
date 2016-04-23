from django import forms
from .models import Municipio,Departamento

class MunicipioForm(forms.ModelForm):
	class Meta:
		model = Municipio
		fields = ["Departamento_id","municipio"]

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = ["departamento"]