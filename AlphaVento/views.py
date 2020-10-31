from django.shortcuts import redirect

def getMain(request):
    response = redirect('/BetaArgenti')
    return response

def login_success(request):
    return redirect('/BetaArgenti')