from django.views.generic import CreateView
from .models import person
from .forms import personform

class home(CreateView):
	model = person
	form_class = personform
	template_name = 'home.html'
