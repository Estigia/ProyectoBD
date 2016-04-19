from django.shortcuts import render
from .forms import UserCreationForm, InicioForm
from .models import Usuario
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

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

		return render(request,'registro.html',context)

	context = {
    	"titulo": "Login"
    }

	return render(request,'login.html',context)

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
    return render(request,'home.html',context)
