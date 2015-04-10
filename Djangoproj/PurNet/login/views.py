from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_user
from django.contrib.auth.forms import AuthenticationForm
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as logout_user

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                return HttpResponseRedirect("/")
    else:
        form = AuthenticationForm()

    return TemplateResponse(request, 'login/login.html', {'form': form})

def logout(request):
    logout_user(request)
    return HttpResponseRedirect("/login/signin")
