from django import forms

class personform(forms.Form):
	CHOICES = (('Male', "Male"),('Female', "Female"))
	name = forms.CharField(label="your name", max_length=100)
	age = forms.IntegerField(label="your age")
	sex = forms.ChoiceField(label="your sex", choices=CHOICES)