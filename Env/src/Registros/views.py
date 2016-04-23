from django.shortcuts import render
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def registro(request):
	form = RegistroForm(request.POST or None)
	

	context = {
		"form" :form,		
		"titulo": "Registros"
	}

	if form.is_valid():
		form.save()


	return render(request,'registros.html',context)
