from django.views.generic import CreateView
from .forms import personform
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        form = personform(request.POST)

        if form.is_valid():
            return redirect('titanicapp:answer')

    else:
        form = personform()

    return render(request, 'home.html', {'form': form})

def answer(request):
    return render(request, 'answer.html', {})

def about(request):
	return render(request, 'about.html')