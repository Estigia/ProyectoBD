from django.shortcuts import render, redirect
from .forms import ArmaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='inicio')
def Arma(request):
	tipo = request.user.Tipo_Usuario_id.id

	if tipo == 4 or tipo == 3:
		form = ArmaForm(request.POST or None)
		context = {
			"form":form,
			"titulo":"Registro de Armas"
		}

		if form.is_valid():
			form.save()
			return redirect('registros:reg')


		return render(request,'armas.html',context)
	else:
		redirect('appHome:403')

def VistaArma(request):
		id_Categoria = request.GET['id']
		muni = Municipio.objects.filter(Departamento_id= id_Departamento)
		data = serializers.serialize('json', muni, fields = ('municipio'))
		return HttpResponse(data, content_type='application/json')
