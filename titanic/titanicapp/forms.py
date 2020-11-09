from django import forms
from .models import person

class personform(forms.ModelForm):
	class Meta:
		model = person
		fields = ['name', 'sex', 'age',]
