# coding: utf-8
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset, password_reset_confirm
#from reviews.models import Review
from authy.forms import SignUpForm
from authy.models import Site_User
from qa.models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'There were some problems while creating your account. Please review some fields before submiting again.')
            context = RequestContext(request, {'form': form})
            return render_to_response('auth/signup.html', context)
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            _user = authenticate(username=username, password=password)
            Site_User.objects.create(user=_user)
            UserProfile.objects.create(user=_user)
            messages.add_message(request, messages.SUCCESS, 'Your account was successfully created.')
            return HttpResponseRedirect("/signup")
    else:
        context = RequestContext(request,  {'form': SignUpForm() })
        return render_to_response('auth/signup.html', context)