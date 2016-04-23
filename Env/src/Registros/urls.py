from django.conf.urls import url
from .views import registro,lista, RegistroDetail

urlpatterns = [

	url(r'^$',registro,name='reg'),
	url(r'^list',lista, name = 'list'),
	url(r'^(?P<pk>\d+)$', RegistroDetail.as_view(), name='detail'),
]