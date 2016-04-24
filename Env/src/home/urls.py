from django.conf.urls import url
from .views import UserDetail, lista, UserUpdate, privado
from Registros.views import listaDetalles
from .views import (

	UserDetail,
	lista, 
	UserUpdate, 
	privado,
	permisos

	)

urlpatterns = [

	url(r'^list',lista, name = 'list'),
	url(r'^(?P<pk>\d+)$', UserDetail.as_view(), name='detail'),
	url(r'^editar/(?P<pk>\d+)$', UserUpdate.as_view(), name='edit'),
	url(r'^$', privado, name = 'perfil'),
	url(r'^perm', permisos, name='403'),
	url(r'^detalles',listaDetalles,name='detail_list')
]