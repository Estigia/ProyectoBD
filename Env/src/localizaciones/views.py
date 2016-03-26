from django.shortcuts import render
from .forms import LocalizacionForm,MunicipioForm,DepartamentoForm

# Create your views here.

def localizacion(request):

	form = DepartamentoForm(request.POST or None)
	form2 = MunicipioForm(request.POST or None)
	form3 = LocalizacionForm(request.POST or None)

	context = {

		"form":form,
		"form2":form2,
		"form3":form3,
		"titulo": "Registro"

	}

	if form.is_valid():
		form.save()
	if form2.is_valid():
		form2.save()
	if form3.is_valid():
		form3.save()

	return render(request,'localizacion.html',context)

