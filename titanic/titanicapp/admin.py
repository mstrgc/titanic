from django.contrib import admin
from .models import person

class PersonPanel(admin.ModelAdmin):
	list_display = ['name', 'age', 'sex',]
	
admin.site.register(person, PersonPanel)