from django.views.generic import CreateView
from .forms import personform
from django.shortcuts import render, redirect
from django.http import HttpResponse
from extentions.ml_titan import got

def home(request):
    if request.method == 'POST':
        form = personform(request.POST)

        if form.is_valid():
            return form.save()

    else:
        form = personform()

    return render(request, 'home.html', {'form': form})

def answer(request):
	a = request.POST['age']
	b = request.POST['sex']
	ct = {
		'name' : request.POST['name'],
		'age' : a,
		'sex' : b,
		'ad' : got(a, b)
	}
	return render(request, 'answer.html', ct)

def about(request):
	return render(request, 'about.html')