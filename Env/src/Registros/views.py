from django.shortcuts import render
from .forms import RegistroForm, VictimaForm

def registro(request):
	form = RegistroForm(request.POST or None)
	form2 = VictimaForm(request.POST or None)

	context = {
		"form" :form,
		"form2" : form2,
		"titulo": "Registros"
	}

	if form.is_valid():
		form.save()
	if form2.is_valid():
		form2.save()

	return render(request,'registros.html',context)
