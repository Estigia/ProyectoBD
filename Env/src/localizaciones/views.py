from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.core import serializers
from django.http import HttpResponse
<<<<<<< HEAD
from .forms import MunicipioForm,DepartamentoForm
from .models import Municipio,Departamento
=======
from .forms import LocalizacionForm,MunicipioForm,DepartamentoForm
from .models import Municipio,Departamento,Localizacion
from django.contrib.auth.decorators import login_required
>>>>>>> 6b38f49ec105d729dc695f409db932e5529b9bce


# Create your views here.
# @login_required('/signin')
# def localizacion(request):

# 	#form = DepartamentoForm(request.POST or None)
# 	#form2 = MunicipioForm(request.POST or None)
# 	#form3 = LocalizacionForm(request.POST or None)
# 	form = LocalizacionForm(request.POST or None)
# 	Departamentos = Departamento.objects.all()
# 	Municipios = Municipio.objects.all()	

<<<<<<< HEAD
	#form = DepartamentoForm(request.POST or None)
	#form2 = MunicipioForm(request.POST or None)
	#form3 = LocalizacionForm(request.POST or None)
	
	Departamentos = Departamento.objects.all()
	Municipios = Municipio.objects.all()	
=======
# 	context = {
>>>>>>> 6b38f49ec105d729dc695f409db932e5529b9bce

# 		#"form":form,
# 		#"form2":form2,
# 		#"form3":form3,
# 		"Departamentos": Departamentos,
# 		"Municipios": Municipios,
# 		"form": form,
# 		"titulo": "Registro"

<<<<<<< HEAD
		#"form":form,
		#"form2":form2,
		#"form3":form3,
		"Departamentos": Departamentos,
		"Municipios": Municipios,
		#"form": form,
		"titulo": "Registro"
=======
# 	}
>>>>>>> 6b38f49ec105d729dc695f409db932e5529b9bce

# 	if form.is_valid():
# 		form.save()
# 	#if form2.is_valid():
# 	#	form2.save()
# 	#if form3.is_valid():
# 	#	form3.save()

<<<<<<< HEAD
	# if form.is_valid():
	# 	form.save()
	#if form2.is_valid():
	#	form2.save()
	#if form3.is_valid():
	#	form3.save()
=======
>>>>>>> 6b38f49ec105d729dc695f409db932e5529b9bce

# 	return render(request,'localizacion.html',context)

def BusquedaMunicipio(request):
		id_Departamento = request.GET['id']
		muni = Municipio.objects.filter(Departamento_id= id_Departamento)		
		print muni
		data = serializers.serialize('json', muni, fields = ('municipio'))
		print data		
		return HttpResponse(data, content_type='application/json')