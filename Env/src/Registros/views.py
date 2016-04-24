from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro, Actividad
from django.core.urlresolvers import reverse_lazy, reverse
#from home.models import Usuario
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from localizaciones.models import Municipio, Departamento
from Armas.models import Arma
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect

class RegistroDetail(LoginRequiredMixin,DetailView):
	login_url = 'inicio'
	model = Registro
	template_name = 'registro_detail.html'

class RegistroUpdate(LoginRequiredMixin,UpdateView):
	login_url = 'inicio'
	model = Registro
	template_name = 'registro_update.html'
	success_url = reverse_lazy('registros:list')
	fields = [

		"nombres",
		"apellidos",
		"edad",
		"muerto",
		"profesion",
		"cui",
		"sexo",
		"ubicacion",
		"fiscal",
		"Municipio",
		"Arma",
		"no_casquillos",
		"serial",
		"fecha",
		"descripcion",
		"is_active",
		"movil",
		"no_expediente"

		]

	def get_context_data(self, **kwargs):
		context = super(RegistroUpdate, self).get_context_data(**kwargs)
		Departamentos = Departamento.objects.all()
		Municipios = Municipio.objects.all()
		Armas = Arma.objects.all()

		context.update({
			"Armas":Armas, 
			"Departamentos":Departamentos,
			"Municipios": Municipios,
			})

		return context

@login_required(login_url='inicio')
def registro(request):

	tipo = request.user.Tipo_Usuario_id.id

	if tipo == 4 or tipo == 3:
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
			rID = form.save()
			vID = request.user
			#rID = Registro.objects.latest('id')
			print vID," ",rID
			a = Actividad(Registro_id=rID,Usuario_id=vID,actividad="Creado")
			a.save()
			return redirect("registros:msg")



		return render(request,'registros.html',context)

	return redirect('appHome:403')

@login_required(login_url='inicio')
def lista(request):
	tipo = request.user.Tipo_Usuario_id.id
	registros = Registro.objects.all()

	if tipo == 4 or tipo == 3:
		context = { "registros": registros }
		return render(request,"registro_list.html",context)

	return redirect('appHome:403')

@login_required(login_url='inicio')
def listaDetalles(request):
	tipo = request.user.Tipo_Usuario_id.id

	if tipo == 4 or tipo == 3:
		detalles = Actividad.objects.all()

		context = {"detalles": detalles}
		return render(request,"detalles_list.html",context)

	return redirect("appHome:403")

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
		data = serializers.serialize('json', Armas, fields = ('objeto','marca','calibre'))
		print data
		return HttpResponse(data, content_type='application/json')

@login_required(login_url='inicio')
def correcto(request):
	tipo = request.user.Tipo_Usuario_id.id
	if tipo == 4 or tipo == 3:
		return render(request, 'agregado.html', {})

	return redirect('appHome:403')