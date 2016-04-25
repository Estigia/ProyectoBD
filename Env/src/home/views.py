# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django import forms
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import UserCreationForm, InicioForm, UserChangeForm
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
from localizaciones.models import Departamento, Municipio
from Armas.models import Arma
# Create your views here.

@login_required(login_url='inicio')
def permisos(request):
    return render(request,'403.html',{})

@login_required(login_url='inicio')
def cambioPass(request):
    form = UserChangeForm(request.POST or None)

    context = { "form": form }

    if form.is_valid():

        password = request.POST['password1']
        usuario = request.user
        #actual = form.cleaned_data.get("actual_pass",usuario.get_password())
        usuario.set_password(password)
        usuario.save()

        logout(request)
        return redirect('/signin')

    return render(request,'cambioPass.html',context)


class UserDetail(LoginRequiredMixin, DetailView):
    login_url = 'inicio'
    model = Usuario
    template_name = 'usuario_detail.html'

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'inicio'
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
    tipo = request.user.Tipo_Usuario_id.id

    if tipo == 4:
        return render(request,'perfil_a.html',{"user": user})
    elif tipo == 3:
        return render(request,'perfil_p.html',{"user":user})

    return render(request,'perfil.html',{"user":user})


def registro(request):
    if not request.user.is_authenticated():

        form = UserCreationForm(request.POST or None)
        context = {
            "form":form,
            "titulo": "Registro"
        }

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signin')

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
                        if request.GET['next'] != '/logout':
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
    Registro_AvM = Registro.objects.filter(Municipio__Departamento_id = 1 , sexo = "M" )
    Registro_AvF = Registro.objects.filter(Municipio__Departamento_id = 1 , sexo = "F" )
    Registro_AvD = Registro.objects.filter(Municipio__Departamento_id = 1 , sexo = "D" )
    Casos_AvM = len(Registro_AvM)
    Casos_AvF = len(Registro_AvF)
    Casos_AvD = len(Registro_AvD)
    Registro_BvM = Registro.objects.filter(Municipio__Departamento_id = 2 , sexo = "M" )
    Registro_BvF = Registro.objects.filter(Municipio__Departamento_id = 2 , sexo = "F" )
    Registro_BvD = Registro.objects.filter(Municipio__Departamento_id = 2 , sexo = "D" )
    Casos_BvM = len(Registro_BvM)
    Casos_BvF = len(Registro_BvF)
    Casos_BvD = len(Registro_BvD)
    Registro_AvE = Registro.objects.filter(Municipio__Departamento_id = 1 ,edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18] )
    Casos_AvE = len(Registro_AvE)
    Registro_BvE = Registro.objects.filter(Municipio__Departamento_id = 2 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18] )
    Casos_BvE = len(Registro_BvE)

    vDep = Departamento.objects.all()
    
    context = {
    
        "Registro_AvM": Casos_AvM,
        "Registro_AvF": Casos_AvF,
        "Registro_AvD": Casos_AvD,
        "Registro_BvM": Casos_BvM,
        "Registro_BvF": Casos_BvF,
        "Registro_BvD": Casos_BvD,
        "Registro_AvE": Casos_AvE,
        "Registro_BvE": Casos_BvE,
        "Deps": vDep,
        # "Registro_Cm": Casos_Cm,
    }
    return render(request,'home.html', context)

class DepDetail(DetailView):
    model = Departamento
    template_name = "dep_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DepDetail,self).get_context_data(**kwargs)
        Departamentos = Departamento.objects.all()
        Municipios = Municipio.objects.all()
        Armas = Arma.objects.all()

        context.update({

            "Armas": Armas,
            "Departamentos": Departamentos,
            "Municipios": Municipios,

            })

        return context
