"""PeriodicoDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from Registros.views import BusquedaMunicipio, BusquedaArma
from home.views import DepDetail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('home.urls', namespace='appHome')),
    url(r'^registro/', 'home.views.registro', name='Registro'),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^regArmas/', 'Armas.views.Arma', name='arma'),
    url(r'^regLocal/', BusquedaMunicipio, name='Local'),
    url(r'^regArma/', BusquedaArma, name='Arma'),
    url(r'^registros/', include('Registros.urls',namespace='registros')),
    url(r'^logout/','home.views.cerrar', name='logout'),
    url(r'^signin/','home.views.inicio', name='inicio'),
    url(r'^estadisticas/', 'home.views.estadisticas', name='estadisticas'),
    url(r'^(?P<pk>\d+)$',DepDetail.as_view(),name='mapa'),
    url(r'^acerca/','home.views.acerca', name='acerca'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
