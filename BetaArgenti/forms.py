from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
    email = forms.EmailField(label = "Your email", required = True)
    name = forms.CharField(label = "Name", required = True)
    isTeacher = forms.BooleanField(label = "I am a Teacher")
    class Meta:
        model = User
        fields = [
            'username', 'name', 'email', 
            'password1', 'password2', 'isTeacher'
        ]