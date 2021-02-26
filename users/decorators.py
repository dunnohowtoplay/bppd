from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('apps:home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'client':
			return HttpResponse("It's Admin only privilege")

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function