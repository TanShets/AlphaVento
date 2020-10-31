from django.shortcuts import render
from .models import Subject
from .forms import UserRegForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView

def getHome(request):
	words = ['Yeah yeah', 'nope', 'Yesterday']
	title = "Welcome home"
	context = {'words': words, 'title': title}
	return render(request, 'BetaArgenti/BetaArgenti_home.html', context)

def goAbout(request):
	print("Reached here")
	context = {
		'name': "Tanish Shetty", 'username': "TanShets",
		'email': "shettytanish02@gmail.com",
		'subjects': ["wide", "bro", "yes", "yep"], 
		'chats': ["Hickigaya", "Yui", "Yukino", "Totsuka", "Hayato", "Haruno"], 
		'title': "Profile"
	}
	return render(request, 'BetaArgenti/profile.html', context)

def viewSubjects(request):
	subjects = Subject.objects.all()
	context = {'subjects': subjects, 'title': "View Subjects"}
	return render(request, 'BetaArgenti/subjects.html', context)

def viewSubject(request):
	#subject = Subject.objects.get(id = subject_id)
	context = {'title': "SubjectName"}
	return render(request, 'BetaArgenti/subject.html', context)

def createAccount(request):
	if request.method == 'POST':
		form = UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Username: {username} created!')
			return redirect('default')
	else:
		form = UserRegForm()
	return render(request, 'BetaArgenti/create.html', {'form': form})

def login_success(request):
	return redirect('default')