from django.contrib import admin
from .models import Subject, Message, Profile

admin.site.register(Subject)
admin.site.register(Message)
admin.site.register(Profile)