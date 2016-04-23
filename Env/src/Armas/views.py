from django.shortcuts import render
from .forms import ArmaForm
from .forms import Tipo_ArmaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='inicio')
def Arma(request):

	form2 = ArmaForm(request.POST or None)
	form = Tipo_ArmaForm(request.POST or None)
	context = {
		"form":form,
		"form2":form2,
		"titulo":"Registro de Armas"
	}

	if form.is_valid():
		form.save()
	if form2.is_valid():
		form2.save()


	return render(request,'armas.html',context)