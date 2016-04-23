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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('home.urls', namespace='appHome')),
    url(r'^registro/', 'home.views.registro', name='Registro'),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^regArmas/', 'Armas.views.Arma', name='arma'),
    #url(r'^regLocalizacion/', 'localizaciones.views.localizacion', name='localizacion'),
    url(r'^regLocal/', BusquedaMunicipio, name='Local'),
<<<<<<< HEAD
    url(r'^regArma/', BusquedaArma, name='Arma'),
    url(r'^registros/', 'Registros.views.registro', name='registros'),
=======
    url(r'^registros/', include('Registros.urls',namespace='registros')),
>>>>>>> 6b38f49ec105d729dc695f409db932e5529b9bce
    url(r'^logout/','home.views.cerrar', name='logout'),
    url(r'^signin/','home.views.inicio', name='inicio'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
