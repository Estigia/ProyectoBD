from django.shortcuts import render
from .forms import RegistroForm
from django.core import serializers
from django.http import HttpResponse
from localizaciones.models import Municipio, Departamento
from Armas.models import Arma
from django.contrib.auth.decorators import login_required


@login_required(login_url='inicio')
def registro(request):
	form = RegistroForm(request.POST or None)
	Departamentos = Departamento.objects.all()
	Municipios = Municipio.objects.all()
	Armas = Arma.objects.all()

	context = {
		"form" :form,		
		"Armas" : Armas,
		"Departamentos" : Departamentos,
		"Municipios" : Municipios,
		"titulo": "Registros"
	}

	if form.is_valid():
		form.save()


	return render(request,'registros.html',context)


def BusquedaMunicipio(request):
		id_Departamento = request.GET['id']
		muni = Municipio.objects.filter(Departamento_id= id_Departamento)		
		data = serializers.serialize('json', muni, fields = ('municipio'))	
		return HttpResponse(data, content_type='application/json')

def BusquedaArma(request):
		id_Arma = request.GET['id']
		print id_Arma
		print id_Arma
		Armas = Arma.objects.filter(categoria = id_Arma)				
		data = serializers.serialize('json', Armas, fields = ('objeto'))
		print data		
		return HttpResponse(data, content_type='application/json')