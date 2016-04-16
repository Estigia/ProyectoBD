from django.shortcuts import render
from .forms import UserCreationForm, InicioForm
from .models import Usuario

# Create your views here.
def registro(request):

	form = UserCreationForm(request.POST or None)
	context = {
		"form":form,
		"titulo": "Registro"
	}

	if form.is_valid():
		form.save()

	return render(request,'registro.html',context)

def inicio(request):

    if request.user.is_authenticated():

    	context = {
    		"titulo": "Login"
    	}

    	return render(request,'login.html',context)
    	
    else:

		form = InicioForm(request.POST or None)
		context = {
			"form":form,
			"titulo": "Inicio"
		}
		#if form.is_valid():
		return render(request,'inicio.html',context)
	 	


