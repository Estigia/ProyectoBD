from django.conf.urls import url
from .views import (
	registro,
	lista, 
	RegistroDetail, 
	RegistroUpdate
	)

urlpatterns = [

	url(r'^$',registro,name='reg'),
	url(r'^list',lista, name = 'list'),
	url(r'^(?P<pk>\d+)$', RegistroDetail.as_view(), name='detail'),
	url(r'^editar/(?P<pk>\d+)$',RegistroUpdate.as_view(), name = 'edit')
]