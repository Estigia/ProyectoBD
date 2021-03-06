from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro, Actividad
from django.core.urlresolvers import reverse_lazy, reverse
#from home.models import Usuario
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from localizaciones.models import Municipio, Departamento
from Armas.models import Arma
from home.models import Usuario
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import ModelFormMixin

class RegistroDetail(DetailView):
	model = Registro
	template_name = 'registro_detail.html'

	@method_decorator(login_required)
	def dispatch(self,request, *args, **kwargs):
		tipo = request.user.Tipo_Usuario_id.id

		if tipo == 4 or tipo == 3:
			return super(RegistroDetail, self).dispatch(request,*args,**kwargs)

		return redirect('appHome:403')

class RegistroUpdate(UpdateView):
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


	def form_valid(self, form):

		self.object = form.save()
		rID = self.object
		vID = self.request.user

		a = Actividad(Registro_id = rID, Usuario_id = vID, actividad = "Modificado")
		a.save()

		return super(RegistroUpdate, self).form_valid(form)

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

	@method_decorator(login_required)
	def dispatch(self,request, *args, **kwargs):
		
		tipo = request.user.Tipo_Usuario_id.id

		if tipo == 4 or tipo == 3:

			return super(RegistroUpdate, self).dispatch(request,*args,**kwargs)

		return redirect('appHome:403')


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
		context = { 
			"registros": registros,
			"bandera": True, 
			}

		return render(request,"registro_list.html",context)

	if tipo == 2:
		registros = Registro.objects.filter(is_active=True)
		context = {
			"registros": registros,
			"bandera": False,
			}

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

@login_required(login_url='inicio')
def detallesUser(request,vID):
	tipo = request.user.Tipo_Usuario_id.id

	if tipo == 4 or tipo == 3:
		detalles = Actividad.objects.filter(Usuario_id=vID)
		usuario = Usuario.objects.filter(id=vID)

		context = {
			"detalles": detalles,
			"usuario": usuario,
		}
		return render(request,"detailList.html",context)

	return redirect("appHome:403")	

def BusquedaMunicipio(request):
	id_Departamento = request.GET['id']
	muni = Municipio.objects.filter(Departamento_id= id_Departamento)
	data = serializers.serialize('json', muni, fields = ('municipio'))
	return HttpResponse(data, content_type='application/json')

def BusquedaArma(request):
		id_Arma = request.GET['id']
		Armas = Arma.objects.filter(categoria = id_Arma)
		data = serializers.serialize('json', Armas, fields = ('objeto','marca','calibre'))
		return HttpResponse(data, content_type='application/json')

@login_required(login_url='inicio')
def correcto(request):
	tipo = request.user.Tipo_Usuario_id.id
	if tipo == 4 or tipo == 3:
		return render(request, 'agregado.html', {})

	return redirect('appHome:403')

def BuscarPorNombre(request):
	search = request.GET['buscar']
	seleccionado = request.GET['select']

	if seleccionado == "Nombre":
		Reg_Nombre = Registro.objects.filter(nombres__contains = search)
		data = serializers.serialize('json', Reg_Nombre, fields = ('Arma','nombres','apellidos','edad',
																'sexo','ubicacion','fecha','descripcion','Municipio'))
	elif seleccionado == "Apellidos":	
		Reg_Nombre = Registro.objects.filter(apellidos__contains = search)
		data = serializers.serialize('json', Reg_Nombre, fields = ('Arma','nombres','apellidos','edad',
																'sexo','ubicacion','fecha','descripcion','Municipio'))
	elif seleccionado == "Edad":	
		Reg_Nombre = Registro.objects.filter(edad__contains = search)
		data = serializers.serialize('json', Reg_Nombre, fields = ('Arma','nombres','apellidos','edad',
																'sexo','ubicacion','fecha','descripcion','Municipio'))
	elif seleccionado == "Sexo":	
		Reg_Nombre = Registro.objects.filter(sexo__contains = search)
		data = serializers.serialize('json', Reg_Nombre, fields = ('Arma','nombres','apellidos','edad',
																'sexo','ubicacion','fecha','descripcion','Municipio'))
	elif seleccionado == "Fecha":	
		Reg_Nombre = Registro.objects.filter(fecha__contains = search)
		data = serializers.serialize('json', Reg_Nombre, fields = ('Arma','nombres','apellidos','edad',
																'sexo','ubicacion','fecha','descripcion','Municipio'))


	return HttpResponse(data, content_type='application/json')