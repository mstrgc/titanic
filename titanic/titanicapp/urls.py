from django.urls import path
from .views import home, answer, about

app_name = 'titanicapp'
urlpatterns = [
	path('', home, name="home"),
	path('answer/', answer, name="answer"),
	path('about-us/', about, name="about-us"),
]