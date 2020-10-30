from django.shortcuts import render
from django.http import HttpResponse

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