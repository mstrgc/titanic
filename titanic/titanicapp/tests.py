from django.test import TestCase
from .forms import PersonForm

class MyTest(TestCase):
	def form_test(self):
		form_data = {'name': 'some name', 'age': 33, 'sex': 'male'}
		form = PersonForm(data=form_data)
		self.assertTrue(form.is_valid())

	def form_none_test(self):
		form_data = {'name': None, 'age': None, 'sex': None}
		form = PersonForm(data=form_data)
		self.assertFalse(form.is_valid())

	def form_wrong_age_test(self):
		form_data = {'name': 'some name', 'age': 'no age', 'sex': 'male'}
		form = PersonForm(data=form_data)
		self.assertFalse(form.is_valid())