from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth

def login(request):

	if request.method == 'GET':
		if request.user.is_authenticated() :
			return render(request, 'index.html')
		else:
			return render(request, 'login.html') 
	else :
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request,user)
			return render(request, 'index.html') 
		else:
			return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'login.html')
