from django.conf.urls import url
from .views import registro,lista

urlpatterns = [

	url(r'^$',registro,name='reg'),
	url(r'^list',lista, name = 'list'),
]