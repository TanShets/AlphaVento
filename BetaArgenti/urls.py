from django.urls import path
from . import views

urlpatterns = [
	path('', views.getHome, name = "homepage"),
	path('/about', views.goAbout, name = "about")
]