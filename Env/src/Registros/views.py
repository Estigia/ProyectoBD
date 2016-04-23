from django.shortcuts import render
from .forms import RegistroForm
from .models import Registro, Actividad
#from home.models import Usuario
from django.contrib.auth.decorators import login_required


@login_required(login_url='inicio')
def registro(request):
	form = RegistroForm(request.POST or None)
	

	context = {
		"form" :form,		
		"titulo": "Registros"
	}

	if form.is_valid():
		rID = form.save()
		vID = request.user
		#rID = Registro.objects.latest('id')
		print vID," ",rID 
		a = Actividad(Registro_id=rID,Usuario_id=vID,actividad="Creado")
		a.save()


	return render(request,'registros.html',context)


@login_required(login_url='inicio')
def lista(request):
    registros = Registro.objects.all()
    context = { "registros": registros }
    return render(request,"registro_list.html",context)