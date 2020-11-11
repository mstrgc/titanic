from django.views.generic import CreateView
from .forms import personform
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        form = personform(request.POST)

        if form.is_valid():
            return form.save()

    else:
        form = personform()

    return render(request, 'home.html', {'form': form})

def answer(request):
	ct = {
		'name' : request.POST['name'],
		'age' : request.POST['age'],
		'sex' : request.POST['sex'],
	}
	return render(request, 'answer.html', ct)

def about(request):
	return render(request, 'about.html')