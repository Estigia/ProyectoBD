# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django import forms
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import UserCreationForm, InicioForm, UserChangeForm
from .models import Usuario
from Registros.models import Actividad
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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


class UserDetail(DetailView):
    model = Usuario
    template_name = 'usuario_detail.html'

    @method_decorator(login_required)
    def dispatch(self,request, *args, **kwargs):
        tipo = request.user.Tipo_Usuario_id.id

        if tipo == 4:
            return super(UserDetail, self).dispatch(request,*args,**kwargs)

        return redirect('appHome:403')

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'inicio'
    model = Usuario
    template_name = 'usuario_update.html'
    success_url = reverse_lazy('appHome:list')
    fields = ['Tipo_Usuario_id', 'is_active']

    @method_decorator(login_required)
    def dispatch(self,request, *args, **kwargs):
        tipo = request.user.Tipo_Usuario_id.id

        if tipo == 4:
            return super(RegistroUpdate, self).dispatch(request,*args,**kwargs)

        return redirect('appHome:403')

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
    Registro_CmM = Registro.objects.filter(Municipio__Departamento_id = 3 , sexo = "M" )
    Registro_CmF = Registro.objects.filter(Municipio__Departamento_id = 3 , sexo = "F" )
    Registro_CmD = Registro.objects.filter(Municipio__Departamento_id = 3 , sexo = "D" )
    Casos_CmM = len(Registro_CmM)
    Casos_CmF = len(Registro_CmF)
    Casos_CmD = len(Registro_CmD)
    Registro_CqM = Registro.objects.filter(Municipio__Departamento_id = 4 , sexo = "M" )
    Registro_CqF = Registro.objects.filter(Municipio__Departamento_id = 4 , sexo = "F" )
    Registro_CqD = Registro.objects.filter(Municipio__Departamento_id = 4 , sexo = "D" )
    Casos_CqM = len(Registro_CqM)
    Casos_CqF = len(Registro_CqF)
    Casos_CqD = len(Registro_CqD)
    Registro_PrM = Registro.objects.filter(Municipio__Departamento_id = 5 , sexo = "M" )
    Registro_PrF = Registro.objects.filter(Municipio__Departamento_id = 5 , sexo = "F" )
    Registro_PrD = Registro.objects.filter(Municipio__Departamento_id = 5 , sexo = "D" )
    Casos_PrM = len(Registro_PrM)
    Casos_PrF = len(Registro_PrF)
    Casos_PrD = len(Registro_PrD)
    Registro_EsM = Registro.objects.filter(Municipio__Departamento_id = 6 , sexo = "M" )
    Registro_EsF = Registro.objects.filter(Municipio__Departamento_id = 6 , sexo = "F" )
    Registro_EsD = Registro.objects.filter(Municipio__Departamento_id = 6 , sexo = "D" )
    Casos_EsM = len(Registro_EsM)
    Casos_EsF = len(Registro_EsF)
    Casos_EsD = len(Registro_EsD)
    Registro_GuM = Registro.objects.filter(Municipio__Departamento_id = 7 , sexo = "M" )
    Registro_GuF = Registro.objects.filter(Municipio__Departamento_id = 7 , sexo = "F" )
    Registro_GuD = Registro.objects.filter(Municipio__Departamento_id = 7 , sexo = "D" )
    Casos_GuM = len(Registro_GuM)
    Casos_GuF = len(Registro_GuF)
    Casos_GuD = len(Registro_GuD)
    Registro_HuM = Registro.objects.filter(Municipio__Departamento_id = 8 , sexo = "M" )
    Registro_HuF = Registro.objects.filter(Municipio__Departamento_id = 8 , sexo = "F" )
    Registro_HuD = Registro.objects.filter(Municipio__Departamento_id = 8 , sexo = "D" )
    Casos_HuM = len(Registro_HuM)
    Casos_HuF = len(Registro_HuF)
    Casos_HuD = len(Registro_HuD)
    Registro_IzM = Registro.objects.filter(Municipio__Departamento_id = 9 , sexo = "M" )
    Registro_IzF = Registro.objects.filter(Municipio__Departamento_id = 9 , sexo = "F" )
    Registro_IzD = Registro.objects.filter(Municipio__Departamento_id = 9 , sexo = "D" )
    Casos_IzM = len(Registro_IzM)
    Casos_IzF = len(Registro_IzF)
    Casos_IzD = len(Registro_IzD)
    Registro_JaM = Registro.objects.filter(Municipio__Departamento_id = 10 , sexo = "M" )
    Registro_JaF = Registro.objects.filter(Municipio__Departamento_id = 10 , sexo = "F" )
    Registro_JaD = Registro.objects.filter(Municipio__Departamento_id = 10 , sexo = "D" )
    Casos_JaM = len(Registro_JaM)
    Casos_JaF = len(Registro_JaF)
    Casos_JaD = len(Registro_JaD)
    Registro_JuM = Registro.objects.filter(Municipio__Departamento_id = 11 , sexo = "M" )
    Registro_JuF = Registro.objects.filter(Municipio__Departamento_id = 11 , sexo = "F" )
    Registro_JuD = Registro.objects.filter(Municipio__Departamento_id = 11 , sexo = "D" )
    Casos_JuM = len(Registro_JuM)
    Casos_JuF = len(Registro_JuF)
    Casos_JuD = len(Registro_JuD)
    Registro_PeM = Registro.objects.filter(Municipio__Departamento_id = 12 , sexo = "M" )
    Registro_PeF = Registro.objects.filter(Municipio__Departamento_id = 12 , sexo = "F" )
    Registro_PeD = Registro.objects.filter(Municipio__Departamento_id = 12 , sexo = "D" )
    Casos_PeM = len(Registro_PeM)
    Casos_PeF = len(Registro_PeF)
    Casos_PeD = len(Registro_PeD)
    Registro_QzM = Registro.objects.filter(Municipio__Departamento_id = 13 , sexo = "M" )
    Registro_QzF = Registro.objects.filter(Municipio__Departamento_id = 13 , sexo = "F" )
    Registro_QzD = Registro.objects.filter(Municipio__Departamento_id = 13 , sexo = "D" )
    Casos_QzM = len(Registro_QzM)
    Casos_QzF = len(Registro_QzF)
    Casos_QzD = len(Registro_QzD)
    Registro_QcM = Registro.objects.filter(Municipio__Departamento_id = 14 , sexo = "M" )
    Registro_QcF = Registro.objects.filter(Municipio__Departamento_id = 14 , sexo = "F" )
    Registro_QcD = Registro.objects.filter(Municipio__Departamento_id = 14 , sexo = "D" )
    Casos_QcM = len(Registro_QcM)
    Casos_QcF = len(Registro_QcF)
    Casos_QcD = len(Registro_QcD)
    Registro_ReM = Registro.objects.filter(Municipio__Departamento_id = 15 , sexo = "M" )
    Registro_ReF = Registro.objects.filter(Municipio__Departamento_id = 15 , sexo = "F" )
    Registro_ReD = Registro.objects.filter(Municipio__Departamento_id = 15 , sexo = "D" )
    Casos_ReM = len(Registro_ReM)
    Casos_ReF = len(Registro_ReF)
    Casos_ReD = len(Registro_ReD)
    Registro_SaM = Registro.objects.filter(Municipio__Departamento_id = 16 , sexo = "M" )
    Registro_SaF = Registro.objects.filter(Municipio__Departamento_id = 16 , sexo = "F" )
    Registro_SaD = Registro.objects.filter(Municipio__Departamento_id = 16 , sexo = "D" )
    Casos_SaM = len(Registro_SaM)
    Casos_SaF = len(Registro_SaF)
    Casos_SaD = len(Registro_SaD)
    Registro_SmM = Registro.objects.filter(Municipio__Departamento_id = 17 , sexo = "M" )
    Registro_SmF = Registro.objects.filter(Municipio__Departamento_id = 17 , sexo = "F" )
    Registro_SmD = Registro.objects.filter(Municipio__Departamento_id = 17 , sexo = "D" )
    Casos_SmM = len(Registro_SmM)
    Casos_SmF = len(Registro_SmF)
    Casos_SmD = len(Registro_SmD)
    Registro_SrM = Registro.objects.filter(Municipio__Departamento_id = 18 , sexo = "M" )
    Registro_SrF = Registro.objects.filter(Municipio__Departamento_id = 18 , sexo = "F" )
    Registro_SrD = Registro.objects.filter(Municipio__Departamento_id = 18 , sexo = "D" )
    Casos_SrM = len(Registro_SrM)
    Casos_SrF = len(Registro_SrF)
    Casos_SrD = len(Registro_SrD)
    Registro_SoM = Registro.objects.filter(Municipio__Departamento_id = 19 , sexo = "M" )
    Registro_SoF = Registro.objects.filter(Municipio__Departamento_id = 19 , sexo = "F" )
    Registro_SoD = Registro.objects.filter(Municipio__Departamento_id = 19 , sexo = "D" )
    Casos_SoM = len(Registro_SoM)
    Casos_SoF = len(Registro_SoF)
    Casos_SoD = len(Registro_SoD)
    Registro_SuM = Registro.objects.filter(Municipio__Departamento_id = 20 , sexo = "M" )
    Registro_SuF = Registro.objects.filter(Municipio__Departamento_id = 20 , sexo = "F" )
    Registro_SuD = Registro.objects.filter(Municipio__Departamento_id = 20 , sexo = "D" )
    Casos_SuM = len(Registro_SuM)
    Casos_SuF = len(Registro_SuF)
    Casos_SuD = len(Registro_SuD)
    Registro_ToM = Registro.objects.filter(Municipio__Departamento_id = 21 , sexo = "M" )
    Registro_ToF = Registro.objects.filter(Municipio__Departamento_id = 21 , sexo = "F" )
    Registro_ToD = Registro.objects.filter(Municipio__Departamento_id = 21 , sexo = "D" )
    Casos_ToM = len(Registro_ToM)
    Casos_ToF = len(Registro_ToF)
    Casos_ToD = len(Registro_ToD)
    Registro_ZaM = Registro.objects.filter(Municipio__Departamento_id = 22 , sexo = "M" )
    Registro_ZaF = Registro.objects.filter(Municipio__Departamento_id = 22 , sexo = "F" )
    Registro_ZaD = Registro.objects.filter(Municipio__Departamento_id = 22 , sexo = "D" )
    Casos_ZaM = len(Registro_ZaM)
    Casos_ZaF = len(Registro_ZaF)
    Casos_ZaD = len(Registro_ZaD)





    Registro_AvE = Registro.objects.filter(Municipio__Departamento_id = 1 ,edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_AvE = len(Registro_AvE)
    Registro_BvE = Registro.objects.filter(Municipio__Departamento_id = 2 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_BvE = len(Registro_BvE)
    Registro_CmE = Registro.objects.filter(Municipio__Departamento_id = 3 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_CmE = len(Registro_CmE)
    Registro_CqE = Registro.objects.filter(Municipio__Departamento_id = 4 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_CqE = len(Registro_CqE)
    Registro_PrE = Registro.objects.filter(Municipio__Departamento_id = 5 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_PrE = len(Registro_PrE)
    Registro_EsE = Registro.objects.filter(Municipio__Departamento_id = 6 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_EsE = len(Registro_EsE)
    Registro_GuE = Registro.objects.filter(Municipio__Departamento_id = 7 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_GuE = len(Registro_GuE)
    Registro_HuE = Registro.objects.filter(Municipio__Departamento_id = 8 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_HuE = len(Registro_HuE)
    Registro_IzE = Registro.objects.filter(Municipio__Departamento_id = 9 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_IzE = len(Registro_IzE)
    Registro_JaE = Registro.objects.filter(Municipio__Departamento_id = 10 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_JaE = len(Registro_JaE)
    Registro_JuE = Registro.objects.filter(Municipio__Departamento_id = 11 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_JuE = len(Registro_JuE)
    Registro_PeE = Registro.objects.filter(Municipio__Departamento_id = 12, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_PeE = len(Registro_PeE)
    Registro_QzE = Registro.objects.filter(Municipio__Departamento_id = 13, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_QzE = len(Registro_QzE)
    Registro_QcE = Registro.objects.filter(Municipio__Departamento_id = 14, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_QcE = len(Registro_QcE)
    Registro_ReE = Registro.objects.filter(Municipio__Departamento_id = 15, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_ReE = len(Registro_ReE)
    Registro_SaE = Registro.objects.filter(Municipio__Departamento_id = 16, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SaE = len(Registro_SaE)
    Registro_SmE = Registro.objects.filter(Municipio__Departamento_id = 17, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SmE = len(Registro_SmE)
    Registro_SrE = Registro.objects.filter(Municipio__Departamento_id = 18, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SrE = len(Registro_SrE)
    Registro_SoE = Registro.objects.filter(Municipio__Departamento_id = 19, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SoE = len(Registro_SoE)
    Registro_SuE = Registro.objects.filter(Municipio__Departamento_id = 20, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SuE = len(Registro_SuE)
    Registro_ToE = Registro.objects.filter(Municipio__Departamento_id = 21, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_ToE = len(Registro_ToE)
    Registro_ZaE = Registro.objects.filter(Municipio__Departamento_id = 22, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_ZaE = len(Registro_ZaE)
    
    

    vDep = Departamento.objects.all()

    context = {

        "Registro_AvM": Casos_AvM,
        "Registro_AvF": Casos_AvF,
        "Registro_AvD": Casos_AvD,
        "Registro_AvE": Casos_AvE,
        "Registro_BvM": Casos_BvM,
        "Registro_BvF": Casos_BvF,
        "Registro_BvD": Casos_BvD,        
        "Registro_BvE": Casos_BvE,
        "Registro_CmF": Casos_CmF,
        "Registro_CmD": Casos_CmD,        
        "Registro_CmE": Casos_CmE,
        "Registro_CqF": Casos_CqF,
        "Registro_CqD": Casos_CqD,        
        "Registro_CqE": Casos_CqE,
        "Registro_PrF": Casos_PrF,
        "Registro_PrD": Casos_PrD,        
        "Registro_PrE": Casos_PrE,
        "Registro_EsF": Casos_EsF,
        "Registro_EsD": Casos_EsD,        
        "Registro_EsE": Casos_EsE,
        "Registro_GuF": Casos_GuF,
        "Registro_GuD": Casos_GuD,        
        "Registro_GuE": Casos_GuE,
        "Registro_HuF": Casos_HuF,
        "Registro_HuD": Casos_HuD,        
        "Registro_HuE": Casos_HuE,
        "Registro_IzF": Casos_IzF,
        "Registro_IzD": Casos_IzD,        
        "Registro_IzE": Casos_IzE,
        "Registro_JaF": Casos_JaF,
        "Registro_JaD": Casos_JaD,        
        "Registro_JaE": Casos_JaE,
        "Registro_JuF": Casos_JuF,
        "Registro_JuD": Casos_JuD,        
        "Registro_JuE": Casos_JuE,
        "Registro_PeF": Casos_PeF,
        "Registro_PeD": Casos_PeD,        
        "Registro_PeE": Casos_PeE,
        "Registro_QzF": Casos_QzF,
        "Registro_QzD": Casos_QzD,        
        "Registro_QzE": Casos_QzE,
        "Registro_QcF": Casos_QcF,
        "Registro_QcD": Casos_QcD,        
        "Registro_QcE": Casos_QcE,
        "Registro_ReF": Casos_ReF,
        "Registro_ReD": Casos_ReD,        
        "Registro_ReE": Casos_ReE,
        "Registro_SaF": Casos_SaF,
        "Registro_SaD": Casos_SaD,        
        "Registro_SaE": Casos_SaE,
        "Registro_SmF": Casos_SmF,
        "Registro_SmD": Casos_SmD,        
        "Registro_SmE": Casos_SmE,
        "Registro_SrF": Casos_SrF,
        "Registro_SrD": Casos_SrD,        
        "Registro_SrE": Casos_SrE,
        "Registro_SoF": Casos_SoF,
        "Registro_SoD": Casos_SoD,        
        "Registro_SoE": Casos_SoE,
        "Registro_SuF": Casos_SuF,
        "Registro_SuD": Casos_SuD,        
        "Registro_SuE": Casos_SuE,
        "Registro_ToF": Casos_ToF,
        "Registro_ToD": Casos_ToD,        
        "Registro_ToE": Casos_ToE,
        "Registro_ZaF": Casos_ZaF,
        "Registro_ZaD": Casos_ZaD,        
        "Registro_ZaE": Casos_ZaE,
        "Deps": vDep,
        
    }
    return render(request,'home.html', context)


    

def estadisticas(request):
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
    Registro_CmM = Registro.objects.filter(Municipio__Departamento_id = 3 , sexo = "M" )
    Registro_CmF = Registro.objects.filter(Municipio__Departamento_id = 3 , sexo = "F" )
    Registro_CmD = Registro.objects.filter(Municipio__Departamento_id = 3 , sexo = "D" )
    Casos_CmM = len(Registro_CmM)
    Casos_CmF = len(Registro_CmF)
    Casos_CmD = len(Registro_CmD)
    Registro_CqM = Registro.objects.filter(Municipio__Departamento_id = 4 , sexo = "M" )
    Registro_CqF = Registro.objects.filter(Municipio__Departamento_id = 4 , sexo = "F" )
    Registro_CqD = Registro.objects.filter(Municipio__Departamento_id = 4 , sexo = "D" )
    Casos_CqM = len(Registro_CqM)
    Casos_CqF = len(Registro_CqF)
    Casos_CqD = len(Registro_CqD)
    Registro_PrM = Registro.objects.filter(Municipio__Departamento_id = 5 , sexo = "M" )
    Registro_PrF = Registro.objects.filter(Municipio__Departamento_id = 5 , sexo = "F" )
    Registro_PrD = Registro.objects.filter(Municipio__Departamento_id = 5 , sexo = "D" )
    Casos_PrM = len(Registro_PrM)
    Casos_PrF = len(Registro_PrF)
    Casos_PrD = len(Registro_PrD)
    Registro_EsM = Registro.objects.filter(Municipio__Departamento_id = 6 , sexo = "M" )
    Registro_EsF = Registro.objects.filter(Municipio__Departamento_id = 6 , sexo = "F" )
    Registro_EsD = Registro.objects.filter(Municipio__Departamento_id = 6 , sexo = "D" )
    Casos_EsM = len(Registro_EsM)
    Casos_EsF = len(Registro_EsF)
    Casos_EsD = len(Registro_EsD)
    Registro_GuM = Registro.objects.filter(Municipio__Departamento_id = 7 , sexo = "M" )
    Registro_GuF = Registro.objects.filter(Municipio__Departamento_id = 7 , sexo = "F" )
    Registro_GuD = Registro.objects.filter(Municipio__Departamento_id = 7 , sexo = "D" )
    Casos_GuM = len(Registro_GuM)
    Casos_GuF = len(Registro_GuF)
    Casos_GuD = len(Registro_GuD)
    Registro_HuM = Registro.objects.filter(Municipio__Departamento_id = 8 , sexo = "M" )
    Registro_HuF = Registro.objects.filter(Municipio__Departamento_id = 8 , sexo = "F" )
    Registro_HuD = Registro.objects.filter(Municipio__Departamento_id = 8 , sexo = "D" )
    Casos_HuM = len(Registro_HuM)
    Casos_HuF = len(Registro_HuF)
    Casos_HuD = len(Registro_HuD)
    Registro_IzM = Registro.objects.filter(Municipio__Departamento_id = 9 , sexo = "M" )
    Registro_IzF = Registro.objects.filter(Municipio__Departamento_id = 9 , sexo = "F" )
    Registro_IzD = Registro.objects.filter(Municipio__Departamento_id = 9 , sexo = "D" )
    Casos_IzM = len(Registro_IzM)
    Casos_IzF = len(Registro_IzF)
    Casos_IzD = len(Registro_IzD)
    Registro_JaM = Registro.objects.filter(Municipio__Departamento_id = 10 , sexo = "M" )
    Registro_JaF = Registro.objects.filter(Municipio__Departamento_id = 10 , sexo = "F" )
    Registro_JaD = Registro.objects.filter(Municipio__Departamento_id = 10 , sexo = "D" )
    Casos_JaM = len(Registro_JaM)
    Casos_JaF = len(Registro_JaF)
    Casos_JaD = len(Registro_JaD)
    Registro_JuM = Registro.objects.filter(Municipio__Departamento_id = 11 , sexo = "M" )
    Registro_JuF = Registro.objects.filter(Municipio__Departamento_id = 11 , sexo = "F" )
    Registro_JuD = Registro.objects.filter(Municipio__Departamento_id = 11 , sexo = "D" )
    Casos_JuM = len(Registro_JuM)
    Casos_JuF = len(Registro_JuF)
    Casos_JuD = len(Registro_JuD)
    Registro_PeM = Registro.objects.filter(Municipio__Departamento_id = 12 , sexo = "M" )
    Registro_PeF = Registro.objects.filter(Municipio__Departamento_id = 12 , sexo = "F" )
    Registro_PeD = Registro.objects.filter(Municipio__Departamento_id = 12 , sexo = "D" )
    Casos_PeM = len(Registro_PeM)
    Casos_PeF = len(Registro_PeF)
    Casos_PeD = len(Registro_PeD)
    Registro_QzM = Registro.objects.filter(Municipio__Departamento_id = 13 , sexo = "M" )
    Registro_QzF = Registro.objects.filter(Municipio__Departamento_id = 13 , sexo = "F" )
    Registro_QzD = Registro.objects.filter(Municipio__Departamento_id = 13 , sexo = "D" )
    Casos_QzM = len(Registro_QzM)
    Casos_QzF = len(Registro_QzF)
    Casos_QzD = len(Registro_QzD)
    Registro_QcM = Registro.objects.filter(Municipio__Departamento_id = 14 , sexo = "M" )
    Registro_QcF = Registro.objects.filter(Municipio__Departamento_id = 14 , sexo = "F" )
    Registro_QcD = Registro.objects.filter(Municipio__Departamento_id = 14 , sexo = "D" )
    Casos_QcM = len(Registro_QcM)
    Casos_QcF = len(Registro_QcF)
    Casos_QcD = len(Registro_QcD)
    Registro_ReM = Registro.objects.filter(Municipio__Departamento_id = 15 , sexo = "M" )
    Registro_ReF = Registro.objects.filter(Municipio__Departamento_id = 15 , sexo = "F" )
    Registro_ReD = Registro.objects.filter(Municipio__Departamento_id = 15 , sexo = "D" )
    Casos_ReM = len(Registro_ReM)
    Casos_ReF = len(Registro_ReF)
    Casos_ReD = len(Registro_ReD)
    Registro_SaM = Registro.objects.filter(Municipio__Departamento_id = 16 , sexo = "M" )
    Registro_SaF = Registro.objects.filter(Municipio__Departamento_id = 16 , sexo = "F" )
    Registro_SaD = Registro.objects.filter(Municipio__Departamento_id = 16 , sexo = "D" )
    Casos_SaM = len(Registro_SaM)
    Casos_SaF = len(Registro_SaF)
    Casos_SaD = len(Registro_SaD)
    Registro_SmM = Registro.objects.filter(Municipio__Departamento_id = 17 , sexo = "M" )
    Registro_SmF = Registro.objects.filter(Municipio__Departamento_id = 17 , sexo = "F" )
    Registro_SmD = Registro.objects.filter(Municipio__Departamento_id = 17 , sexo = "D" )
    Casos_SmM = len(Registro_SmM)
    Casos_SmF = len(Registro_SmF)
    Casos_SmD = len(Registro_SmD)
    Registro_SrM = Registro.objects.filter(Municipio__Departamento_id = 18 , sexo = "M" )
    Registro_SrF = Registro.objects.filter(Municipio__Departamento_id = 18 , sexo = "F" )
    Registro_SrD = Registro.objects.filter(Municipio__Departamento_id = 18 , sexo = "D" )
    Casos_SrM = len(Registro_SrM)
    Casos_SrF = len(Registro_SrF)
    Casos_SrD = len(Registro_SrD)
    Registro_SoM = Registro.objects.filter(Municipio__Departamento_id = 19 , sexo = "M" )
    Registro_SoF = Registro.objects.filter(Municipio__Departamento_id = 19 , sexo = "F" )
    Registro_SoD = Registro.objects.filter(Municipio__Departamento_id = 19 , sexo = "D" )
    Casos_SoM = len(Registro_SoM)
    Casos_SoF = len(Registro_SoF)
    Casos_SoD = len(Registro_SoD)
    Registro_SuM = Registro.objects.filter(Municipio__Departamento_id = 20 , sexo = "M" )
    Registro_SuF = Registro.objects.filter(Municipio__Departamento_id = 20 , sexo = "F" )
    Registro_SuD = Registro.objects.filter(Municipio__Departamento_id = 20 , sexo = "D" )
    Casos_SuM = len(Registro_SuM)
    Casos_SuF = len(Registro_SuF)
    Casos_SuD = len(Registro_SuD)
    Registro_ToM = Registro.objects.filter(Municipio__Departamento_id = 21 , sexo = "M" )
    Registro_ToF = Registro.objects.filter(Municipio__Departamento_id = 21 , sexo = "F" )
    Registro_ToD = Registro.objects.filter(Municipio__Departamento_id = 21 , sexo = "D" )
    Casos_ToM = len(Registro_ToM)
    Casos_ToF = len(Registro_ToF)
    Casos_ToD = len(Registro_ToD)
    Registro_ZaM = Registro.objects.filter(Municipio__Departamento_id = 22 , sexo = "M" )
    Registro_ZaF = Registro.objects.filter(Municipio__Departamento_id = 22 , sexo = "F" )
    Registro_ZaD = Registro.objects.filter(Municipio__Departamento_id = 22 , sexo = "D" )
    Casos_ZaM = len(Registro_ZaM)
    Casos_ZaF = len(Registro_ZaF)
    Casos_ZaD = len(Registro_ZaD)





    Registro_AvE = Registro.objects.filter(Municipio__Departamento_id = 1 ,edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_AvE = len(Registro_AvE)
    Registro_BvE = Registro.objects.filter(Municipio__Departamento_id = 2 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_BvE = len(Registro_BvE)
    Registro_CmE = Registro.objects.filter(Municipio__Departamento_id = 3 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_CmE = len(Registro_CmE)
    Registro_CqE = Registro.objects.filter(Municipio__Departamento_id = 4 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_CqE = len(Registro_CqE)
    Registro_PrE = Registro.objects.filter(Municipio__Departamento_id = 5 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_PrE = len(Registro_PrE)
    Registro_EsE = Registro.objects.filter(Municipio__Departamento_id = 6 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_EsE = len(Registro_EsE)
    Registro_GuE = Registro.objects.filter(Municipio__Departamento_id = 7 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_GuE = len(Registro_GuE)
    Registro_HuE = Registro.objects.filter(Municipio__Departamento_id = 8 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_HuE = len(Registro_HuE)
    Registro_IzE = Registro.objects.filter(Municipio__Departamento_id = 9 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_IzE = len(Registro_IzE)
    Registro_JaE = Registro.objects.filter(Municipio__Departamento_id = 10 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_JaE = len(Registro_JaE)
    Registro_JuE = Registro.objects.filter(Municipio__Departamento_id = 11 , edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_JuE = len(Registro_JuE)
    Registro_PeE = Registro.objects.filter(Municipio__Departamento_id = 12, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_PeE = len(Registro_PeE)
    Registro_QzE = Registro.objects.filter(Municipio__Departamento_id = 13, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_QzE = len(Registro_QzE)
    Registro_QcE = Registro.objects.filter(Municipio__Departamento_id = 14, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_QcE = len(Registro_QcE)
    Registro_ReE = Registro.objects.filter(Municipio__Departamento_id = 15, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_ReE = len(Registro_ReE)
    Registro_SaE = Registro.objects.filter(Municipio__Departamento_id = 16, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SaE = len(Registro_SaE)
    Registro_SmE = Registro.objects.filter(Municipio__Departamento_id = 17, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SmE = len(Registro_SmE)
    Registro_SrE = Registro.objects.filter(Municipio__Departamento_id = 18, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SrE = len(Registro_SrE)
    Registro_SoE = Registro.objects.filter(Municipio__Departamento_id = 19, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SoE = len(Registro_SoE)
    Registro_SuE = Registro.objects.filter(Municipio__Departamento_id = 20, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_SuE = len(Registro_SuE)
    Registro_ToE = Registro.objects.filter(Municipio__Departamento_id = 21, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_ToE = len(Registro_ToE)
    Registro_ZaE = Registro.objects.filter(Municipio__Departamento_id = 22, edad__in=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] )
    Casos_ZaE = len(Registro_ZaE)
    
    

    vDep = Departamento.objects.all()
    
    context = {
    
        "Registro_AvM": Casos_AvM,
        "Registro_AvF": Casos_AvF,
        "Registro_AvD": Casos_AvD,
        "Registro_AvE": Casos_AvE,
        "Registro_BvM": Casos_BvM,
        "Registro_BvF": Casos_BvF,
        "Registro_BvD": Casos_BvD,        
        "Registro_BvE": Casos_BvE,
        "Registro_CmF": Casos_CmF,
        "Registro_CmD": Casos_CmD,        
        "Registro_CmE": Casos_CmE,
        "Registro_CqF": Casos_CqF,
        "Registro_CqD": Casos_CqD,        
        "Registro_CqE": Casos_CqE,
        "Registro_PrF": Casos_PrF,
        "Registro_PrD": Casos_PrD,        
        "Registro_PrE": Casos_PrE,
        "Registro_EsF": Casos_EsF,
        "Registro_EsD": Casos_EsD,        
        "Registro_EsE": Casos_EsE,
        "Registro_GuF": Casos_GuF,
        "Registro_GuD": Casos_GuD,        
        "Registro_GuE": Casos_GuE,
        "Registro_HuF": Casos_HuF,
        "Registro_HuD": Casos_HuD,        
        "Registro_HuE": Casos_HuE,
        "Registro_IzF": Casos_IzF,
        "Registro_IzD": Casos_IzD,        
        "Registro_IzE": Casos_IzE,
        "Registro_JaF": Casos_JaF,
        "Registro_JaD": Casos_JaD,        
        "Registro_JaE": Casos_JaE,
        "Registro_JuF": Casos_JuF,
        "Registro_JuD": Casos_JuD,        
        "Registro_JuE": Casos_JuE,
        "Registro_PeF": Casos_PeF,
        "Registro_PeD": Casos_PeD,        
        "Registro_PeE": Casos_PeE,
        "Registro_QzF": Casos_QzF,
        "Registro_QzD": Casos_QzD,        
        "Registro_QzE": Casos_QzE,
        "Registro_QcF": Casos_QcF,
        "Registro_QcD": Casos_QcD,        
        "Registro_QcE": Casos_QcE,
        "Registro_ReF": Casos_ReF,
        "Registro_ReD": Casos_ReD,        
        "Registro_ReE": Casos_ReE,
        "Registro_SaF": Casos_SaF,
        "Registro_SaD": Casos_SaD,        
        "Registro_SaE": Casos_SaE,
        "Registro_SmF": Casos_SmF,
        "Registro_SmD": Casos_SmD,        
        "Registro_SmE": Casos_SmE,
        "Registro_SrF": Casos_SrF,
        "Registro_SrD": Casos_SrD,        
        "Registro_SrE": Casos_SrE,
        "Registro_SoF": Casos_SoF,
        "Registro_SoD": Casos_SoD,        
        "Registro_SoE": Casos_SoE,
        "Registro_SuF": Casos_SuF,
        "Registro_SuD": Casos_SuD,        
        "Registro_SuE": Casos_SuE,
        "Registro_ToF": Casos_ToF,
        "Registro_ToD": Casos_ToD,        
        "Registro_ToE": Casos_ToE,
        "Registro_ZaF": Casos_ZaF,
        "Registro_ZaD": Casos_ZaD,        
        "Registro_ZaE": Casos_ZaE,
        "Deps": vDep,
        }

    return render(request,'estadisticas.html', context)

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


def acerca(request):
    return render(request,'acerca.html', {})
