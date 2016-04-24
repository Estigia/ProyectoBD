#encoding: utf-8

from django import forms
from .models import Usuario
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)
 
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'institucion','nombre_usuario','correo']

    def clean_password1(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        if password1 and password and len(password) < 8:
            raise forms.ValidationError("Ingrese una contraseña mas larga.")
        return password1

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
            
        return user

# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password1 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)
 
#     class Meta:
#         model = Usuario
#         fields = ['nombre', 'apellidos']

#     def clean_password1(self):
#         # Check that the two password entries match
#         password = self.cleaned_data.get("password")
#         password1 = self.cleaned_data.get("password1")
#         if password and password1 and password != password1:
#             raise forms.ValidationError("Las contraseñas no coinciden.")
#         if password1 and password and len(password) < 8:
#             raise forms.ValidationError("Ingrese una contraseña mas larga.")
#         return password1

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserChangeForm, self).save(commit=False)
#         user.set_password(self.cleaned_data.get("password1"))
#         if commit:
#             user.save()
            
#         return user

class UserChangeForm(forms.Form):
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    password1 = forms.CharField(label='Confirmar password',widget=forms.PasswordInput())
    

    def clean_password1(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password and password1 and password != password1:

            raise forms.ValidationError("Las contraseñas no coinciden.")

        if password1 and password and len(password) < 8:

            raise forms.ValidationError("Ingrese una contraseña mas larga.")

        return password1

class InicioForm(forms.Form):
	usuario = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

