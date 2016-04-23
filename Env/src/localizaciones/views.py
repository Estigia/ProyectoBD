from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.core import serializers
from django.http import HttpResponse
from .forms import MunicipioForm,DepartamentoForm
from .models import Municipio,Departamento
from django.contrib.auth.decorators import login_required

def localizacion(request):
	Departamentos = Departamento.objects.all()
	Municipios = Municipio.objects.all()

	context = {

		"Departamentos": Departamentos,
		"Municipios":Municipios,
		"titulo": "localizacion"

	}

	return render(request,'localizacion.html',context)

def BusquedaMunicipio(request):
		id_Departamento = request.GET['id']
		muni = Municipio.objects.filter(Departamento_id= id_Departamento)		
		print muni
		data = serializers.serialize('json', muni, fields = ('municipio'))
		print data		
		return HttpResponse(data, content_type='application/json')