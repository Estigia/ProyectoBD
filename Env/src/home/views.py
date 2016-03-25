from django.shortcuts import render
from .forms import SignForm
from .models import Usuario

# Create your views here.
def inicio(request):

	form = SignForm(request.POST or None)
	context = {
		"form":form
	}

	if form.is_valid():
		form.save()

	return render(request,'inicio.html',context)