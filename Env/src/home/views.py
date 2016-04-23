from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .forms import UserCreationForm, InicioForm
from .models import Usuario
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
)
from .models import Usuario
# Create your views here.

class UserDetail(LoginRequiredMixin, DetailView):
    login_url = 'inicio'
    model = Usuario
    template_name = 'usuario_detail.html'

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'usuario_update.html'
    success_url = reverse_lazy('appHome:list')
    fields = ['Tipo_Usuario_id', 'is_active']

@login_required(login_url='inicio')
def lista(request):
    usuarios = Usuario.objects.all()
    context = { "usuarios": usuarios }
    return render(request,"usuario_list.html",context)

def registro(request):
    if not request.user.is_authenticated():

        form = UserCreationForm(request.POST or None)
        context = {
            "form":form,
            "titulo": "Registro"
        }

        if form.is_valid():
<<<<<<< HEAD
=======
            
>>>>>>> 6b38f49ec105d729dc695f409db932e5529b9bce
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

                    if request.GET:
                        return HttpResponseRedirect(request.GET['next'])

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

@login_required(login_url='inicio')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


def home(request):
	return render(request, 'home.html', {})
