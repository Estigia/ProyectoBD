from django.conf.urls import url
from .views import (

	UserDetail, lista, UserUpdate, privado

	)

urlpatterns = [

	url(r'^list',lista, name = 'list'),
	url(r'^(?P<pk>\d+)$', UserDetail.as_view(), name='detail'),
	url(r'^editar/(?P<pk>\d+)$', UserUpdate.as_view(), name='edit'),
	url(r'^$', privado, name = 'perfil')
]