from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import UserCreationForm, InicioForm
from .models import Usuario
from Registros.models import Actividad
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from Registros.models import Registro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Usuario
from localizaciones.models import Departamento
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

@login_required(login_url='inicio')
def privado(request):
    user = request.user
    detalles = Actividad.objects.filter(Usuario_id = user.id)
    print detalles
    return render(request,'perfil.html',{"user": user})


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

                    return redirect('appHome:perfil')
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
    Registro_Av = Registro.objects.filter(Municipio__Departamento_id = 1)
    Registro_Bv = Registro.objects.filter(Municipio__Departamento_id = 2)
    # Registro_Cv = Registro.objects.filter(Municipio__Departamento_id = 3)
    Casos_Av = len(Registro_Av)
    Casos_Bv = len(Registro_Bv)
    vDep = Departamento.objects.all()
    # Casos_Cm = len(Registro_Cm)
    context = {
        "Registro_Av": Casos_Av,
        "Registro_Bv": Casos_Bv,
        "Deps": vDep,
        # "Registro_Cm": Casos_Cm,
    }
    return render(request,'home.html', context)

class DepDetail(DetailView):
    model = Departamento
    template_name = "dep_detail.html"

