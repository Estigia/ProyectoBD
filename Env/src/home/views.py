from django.shortcuts import render
from .forms import UserCreationForm, InicioForm
from .models import Usuario
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def registro(request):
    if not request.user.is_authenticated():

        form = UserCreationForm(request.POST or None)
        context = {
            "form":form,
            "titulo": "Registro"
        }

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request,'registro.html',context)

    return HttpResponseRedirect('/')
    
def inicio(request):


    if request.user.is_authenticated():

    	context = {
    		"titulo": "Login"
    	}

    	return render(request,'login.html',context)

    if request.POST:

    	form = InicioForm(request.POST or None)

    	if form.is_valid():
    		#instance = form.save(commit=False)

    		username = request.POST['usuario']
    		password = request.POST['password']

    		user = authenticate(username = username, password = password)

    		if user is not None:
    			if user.is_active:
    				login(request, user)
    				context = {
    					"form": form,
    					"titulo": "Login"
    				}
    				return render(request,'login.html',context)
    			else:
    				return HttpResponseRedirect('/')
    		else:
    			return HttpResponseRedirect('/')

    else:
    	form = InicioForm()

    context ={
    	"form": form,
    	"titulo": "Inicio"
    }
    return render(request,'inicio.html',context)

@login_required(login_url='/')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


def home(request):
	return render(request, 'home.html', {})
