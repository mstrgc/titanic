from django.views.generic import CreateView
from .forms import PersonForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from extentions.ml_titan import ml

def home(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            return form.save()

    else:
        form = PersonForm()

    return render(request, 'home.html', {'form': form,})

def answer(request):
	age = request.POST['age']
	sex = request.POST['sex']
	context = {
		'name' : request.POST['name'],
		'age' : age,
		'sex' : sex,
		'ad' : ml(age, sex),
	}
	return render(request, 'answer.html', context)

def about(request):
	return render(request, 'about.html')