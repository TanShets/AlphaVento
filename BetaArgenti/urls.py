from django.urls import path
from . import views, views2

urlpatterns = [
	path('', views.getHome, name = "default"),
	path('/profile', views.goAbout, name = "profile"),
	path('/subjects', views.viewSubjects, name = "subjects"),
	path('/subject', views.viewSubject, name = "subject"),
	path('/create', views.createAccount, name = "create"),
	path('/login', views.LoginView.as_view(template_name = "BetaArgenti/login.html"), name = "login"),
	path('/logout', views.LogoutView.as_view(template_name = "BetaArgenti/logout.html"), name = "logout"),
	path('/accounts/profile', views.login_success, name = "login-success"),
	
	path('/subject/<pk>', views2.SubjectView.as_view(), name = "subject"),
	path('/subject/chat/<pk>', views2.ChatView.as_view(), name = "subject-chat"),
	path('/subject/assignment/<pk>', views2.AssignmentView.as_view(), name = "subject-assignment"),
	path('/subject/members/<pk>', views2.MembersView.as_view(), name = "subject-members"),
	path('/subject/reference/<pk>', views2.ChatView.as_view(), name = "subject-reference")
]