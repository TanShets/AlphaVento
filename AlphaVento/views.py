from django.shortcuts import redirect

def getMain(request):
    response = redirect('/BetaArgenti')
    return response