from django import forms
from .models import Usuario

class SignForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ["nombre",
					"apellidos",
					"contrasena",
					"institucion",
					"nombre_usuario",
					"correo"]

class InicioForm(form.Form):
	usuario = forms.CharField()
	contrasena = forms.CharField(widget=forms.PasswordInput())