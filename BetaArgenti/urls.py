from django.urls import path
from . import views

urlpatterns = [
	path('', views.getHome, name = "default"),
	path('/profile', views.goAbout, name = "profile"),
	path('/subjects', views.viewSubjects, name = "subjects"),
	path('/subject', views.viewSubject, name = "subject"),
	path('/subject/<pk>', views.SubjectView.as_view(), name = "subject"),
	path('/create', views.createAccount, name = "create"),
	path('/login', views.LoginView.as_view(template_name = "BetaArgenti/login.html"), name = "login"),
	path('/logout', views.LogoutView.as_view(template_name = "BetaArgenti/logout.html"), name = "logout"),
	path('/accounts/profile', views.login_success, name = "login-success")
]