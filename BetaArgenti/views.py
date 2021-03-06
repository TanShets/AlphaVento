from django.shortcuts import render
from django.urls import reverse
from .models import Subject
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.utils.decorators import classonlymethod

def getHome(request):
	words = ['Yeah yeah', 'nope', 'Yesterday']
	title = "Welcome home"
	context = {'words': words, 'title': title}
	return render(request, 'BetaArgenti/BetaArgenti_home.html', context)

def goAbout(request):
	#print("Reached here")
	context = {
		'subjects': ["wide", "bro", "yes", "yep"], 
		'chats': ["Hickigaya", "Yui", "Yukino", "Totsuka", "Hayato", "Haruno"], 
		'title': "Profile"
	}
	#print(request.method)
	#print(request.POST)
	if request.method != 'POST':
		context['isEdit'] = 0
		#print(context)
		#print("Here now")
		return render(request, 'BetaArgenti/profile.html', context)
	elif request.POST.get('isEdit', False) == "Start":
		#print(request.POST)
		form1 = UserUpdateXForm()
		form2 = ProfileUpdateForm()
		context['form1'] = form1
		context['form2'] = form2
		context['isEdit'] = 1
		return render(request, 'BetaArgenti/profile.html', context)
	elif request.POST.get('isEdit', False) == "End":
		for_user_form = {
			#'csrfmiddlewaretoken': request.POST.get('csrfmiddlewaretoken', False),
			'username': request.POST.get('username', False),
			'email': request.POST.get('email', False)
		}

		for_profile_form = {
			'name': request.POST.get('name', False)
		}
		#print(request.user.email)
		form1 = UserUpdateXForm(data = for_user_form, instance = request.user)
		form2 = ProfileUpdateForm(data = for_profile_form, instance = request.user.profile)
		if form1.is_valid() and form2.is_valid():
			form1.save()
			form2.save()
			messages.success(request, f'Account Username: {request.user.username} updated!')
			#print("Achieved")
			return redirect('profile')
		else:
			#print(request.POST)
			print("Form User is", form1.is_valid())
			messages.danger(request, f'Account Username: { request.user.username } could not be updated')
			#print(form2.is_valid())
			return redirect('profile')

def viewSubjects(request):
	if request.method != 'POST':
		subjects = Subject.objects.all()
		context = {'subjects': subjects, 'title': "View Subjects"}
		return render(request, 'BetaArgenti/subjects.html', context)
	else:
		new_id = request.POST.get("id", False)
		if new_id:
			return redirect('subject/'+str(new_id))
		else:
			return redirect('subjects')

def viewSubject(request):
	#subject = Subject.objects.get(id = subject_id)
	return render(request, 'BetaArgenti/subject.html')

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