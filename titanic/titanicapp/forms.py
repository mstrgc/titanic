from django import forms

class personform(forms.Form):
	CHOICES = (('Male', "Male"),('Female', "Female"))
	name = forms.CharField(
		label="your name",
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'text-dark fr form-control mx-3 animate__animated animate__fadeInUp'})
	)
	age = forms.IntegerField(
		label="your age",
		widget=forms.NumberInput(attrs={'class': 'text-dark fr form-control mx-3 animate__animated animate__fadeInUp'})
	)
	sex = forms.ChoiceField(
		label="your sex",
		choices=CHOICES,
		widget=forms.Select(attrs={'class': 'text-dark fr form-control mx-3 animate__animated animate__fadeInUp'})
	)