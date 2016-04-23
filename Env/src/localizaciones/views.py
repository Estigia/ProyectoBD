from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.core import serializers
from django.http import HttpResponse
from .forms import MunicipioForm,DepartamentoForm
from .models import Municipio,Departamento


# Create your views here.

def localizacion(request):

	#form = DepartamentoForm(request.POST or None)
	#form2 = MunicipioForm(request.POST or None)
	#form3 = LocalizacionForm(request.POST or None)
	
	Departamentos = Departamento.objects.all()
	Municipios = Municipio.objects.all()	

	context = {

		#"form":form,
		#"form2":form2,
		#"form3":form3,
		"Departamentos": Departamentos,
		"Municipios": Municipios,
		#"form": form,
		"titulo": "Registro"

	}

	# if form.is_valid():
	# 	form.save()
	#if form2.is_valid():
	#	form2.save()
	#if form3.is_valid():
	#	form3.save()


	return render(request,'localizacion.html',context)

def BusquedaMunicipio(request):
		id_Departamento = request.GET['id']
		muni = Municipio.objects.filter(Departamento_id= id_Departamento)		
		print muni
		data = serializers.serialize('json', muni, fields = ('municipio'))
		print data		
		return HttpResponse(data, content_type='application/json')