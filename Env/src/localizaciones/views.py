from django.shortcuts import render
from .forms import LocalizacionForm,MunicipioForm,DepartamentoForm

# Create your views here.

def localizacion(request):

	form = DepartamentoForm
	form2 = MunicipioForm
	form3 = LocalizacionForm

	context = {

		"form":form,
		"form2":form2
		"form3":form3
		"titulo": "Registro"

	}

	if form.is_valid() and form2.is_valid() and form3.is_valid():
		form.save()
		form2.save()
		form3.save()

	return render(request,'localizacion.html',context)

