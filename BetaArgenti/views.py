from django.shortcuts import render
from django.http import HttpResponse

def getHome(request):
	words = ['Yeah yeah', 'nope', 'Yesterday']
	title = "Welcome home"
	context = {'words': words, 'title': title}
	return render(request, 'BetaArgenti/BetaArgenti_home.html', context)