from django.views.generic import CreateView
from .forms import personform
from django.shortcuts import render, redirect
from django.http import HttpResponse
from extentions.ml_titan import ml

def home(request):
    if request.method == 'POST':
        form = personform(request.POST)

        if form.is_valid():
            return form.save()

    else:
        form = personform()

    return render(request, 'home.html', {'form': form,})

def answer(request):
	aa = request.POST['age']
	bb = request.POST['sex']
	ct = {
		'name' : request.POST['name'],
		'age' : aa,
		'sex' : bb,
		'ad' : ml(aa, bb),
	}
	return render(request, 'answer.html', ct)

def about(request):
	return render(request, 'about.html')