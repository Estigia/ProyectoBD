from django.shortcuts import render
from .forms import ArmaForm
from .forms import Tipo_ArmaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='inicio')
def Arma(request):

	form = ArmaForm(request.POST or None)	
	context = {
		"form":form,		
		"titulo":"Registro de Armas"
	}

	if form.is_valid():
		form.save()

	return render(request,'armas.html',context)

def VistaArma(request):
		id_Categoria = request.GET['id']
		muni = Municipio.objects.filter(Departamento_id= id_Departamento)				
		data = serializers.serialize('json', muni, fields = ('municipio'))		
		return HttpResponse(data, content_type='application/json')	