from django.urls import path
from .views import home

app_name = 'titanicapp'
urlpatterns = [
	path('', home.as_view(), name="home")
]