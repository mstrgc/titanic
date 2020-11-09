from django.db import models

class person(models.Model):
	CHOICES = (('Male', "Male"),('Female', "Female"))
	name = models.CharField(max_length=100, null=True)
	sex = models.CharField(max_length=10, choices=CHOICES)
	age = models.IntegerField()

	def __str__(self):
		return self.name