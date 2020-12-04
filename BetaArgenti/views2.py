from django.shortcuts import render
from django.urls import reverse
from .models import Subject
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.utils.decorators import classonlymethod

class SubjectView(DetailView):
	model = Subject
	template_name = 'BetaArgenti/subject.html'
	context_object_name = 'subject'
	
	def get_context_data(self, *args, **kwargs):
		data = super(SubjectView, self).get_context_data(*args, **kwargs)
		data['title'] = data['subject'].title + ' - ' + str(data['subject'].author)
		data['id'] = data['subject'].id
		#print(self.__dict__)
		return data
	
	@classonlymethod
	def as_view(cls, **initkwargs):
		self = cls(**initkwargs)
		view = super(DetailView, cls).as_view(**initkwargs)
		return view
	
	def dispatch(self, request, *args, **kwargs):
		if self.request.GET.get('id', False):
			num = int(self.request.GET.get('link', 0))
			if num == 0:
				return super(SubjectView, self).dispatch(request, *args, **kwargs)
			elif num == 1:
				return redirect('subject-chat', pk = self.request.GET['id'])
			elif num == 2:
				return redirect('subject-members', pk = self.request.GET['id'])
				#return super(SubjectView, self).dispatch(request, *args, **kwargs)
			elif num == 3:
				return redirect('subject-assignment', pk = self.request.GET['id'])
				#return super(SubjectView, self).dispatch(request, *args, **kwargs)
			elif num == 4:
				return redirect('subject-reference', pk = self.request.GET['id'])
				#return super(SubjectView, self).dispatch(request, *args, **kwargs)
		else:
			return super(SubjectView, self).dispatch(request, *args, **kwargs)

class ChatView(DetailView):
	model = Subject
	template_name = 'BetaArgenti/subject_chat.html'
	context_object_name = 'chat'

	def get_context_data(self, *args, **kwargs):
		data = super(ChatView, self).get_context_data(*args, **kwargs)
		data['title'] = data['chat'].title + ' - ' + str(data['chat'].author)
		data['id'] = data['chat'].id
		data['messages'] = data['chat'].messages
		#print(self.__dict__)
		return data

class AssignmentView(DetailView):
	model = Subject
	template_name = 'BetaArgenti/subject_assignments.html'
	context_object_name = 'assignments'

	def get_context_data(self, *args, **kwargs):
		data = super(AssignmentView, self).get_context_data(*args, **kwargs)
		data['title'] = data['assignments'].title + ' - ' + str(data['assignments'].author)
		data['id'] = data['assignments'].id
		data['messages'] = data['assignments'].messages
		#print(self.__dict__)
		return data

class MembersView(DetailView):
	model = Subject
	template_name = 'BetaArgenti/subject_members.html'
	context_object_name = 'members'

	def get_context_data(self, *args, **kwargs):
		data = super(MembersView, self).get_context_data(*args, **kwargs)
		data['title'] = data['members'].title + ' - ' + str(data['members'].author)
		data['id'] = data['members'].id
		data['messages'] = data['members'].messages
		#print(self.__dict__)
		return data

class ReferenceView(DetailView):
	model = Subject
	template_name = 'BetaArgenti/subject_reference.html'
	context_object_name = 'reference'

	def get_context_data(self, *args, **kwargs):
		data = super(ReferenceView, self).get_context_data(*args, **kwargs)
		data['title'] = data['reference'].title + ' - ' + str(data['reference'].author)
		data['id'] = data['reference'].id
		data['messages'] = data['reference'].messages
		#print(self.__dict__)
		return data