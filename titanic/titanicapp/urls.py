from django.urls import path
from .views import home, answer

app_name = 'titanicapp'
urlpatterns = [
	path('', home, name="home"),
	path('answer/', answer, name="answer"),
]