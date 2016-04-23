from django.conf.urls import url
from .views import registro

urlpatterns = [

	url(r'^$',registro,name='list')

]