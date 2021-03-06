from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    messages = models.TextField()
    students = models.TextField()
    creation_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'( id: {self.id}, title: {self.title} )'

class Message(models.Model):
    content = models.TextField()
    message_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 60)
    isTeacher = models.BooleanField(default = False)
    is_final = models.BooleanField(default = False)

    def __str__(self):
        return f'{self.user.username} name: {self.name}'