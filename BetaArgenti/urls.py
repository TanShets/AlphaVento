from django.urls import path
from . import views

urlpatterns = [
	path('', views.getHome, name = "default"),
	path('/profile', views.goAbout, name = "profile"),
	path('/subjects', views.viewSubjects, name = "subjects"),
	path('/subject', views.viewSubject, name = "subject")
]