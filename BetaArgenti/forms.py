from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegForm(UserCreationForm):
    email = forms.EmailField(label = "Your email", required = True)
    #name = forms.CharField(label = "Name", required = True)
    #isTeacher = forms.BooleanField(initial = False, label = "I am a Teacher", required = False)
    class Meta:
        model = User
        fields = [
            'username', 'email', 
            'password1', 'password2',
        ]

class UserUpdateXForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'isTeacher']