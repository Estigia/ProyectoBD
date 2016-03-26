from django.shortcuts import render
from .forms import ArmaForm
form .forms import Tipo_ArmaForm


# Create your views here.
def Arma(request):

	form = SignForm(request.POST or None)
	form2 = SignForm(request.POST or None)
	context = {
		"form":form
		"form2":form2
		"titulo":Registro de Armas
	}

	if form.is_valid():
		form.save()
	if form2.is_valid():
		form2.is_valid():


	return render(request,'Arma.html',context)