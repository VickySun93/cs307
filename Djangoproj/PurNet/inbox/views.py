from django.shortcuts import render
from django.template.response import TemplateResponse
from inbox.models import Message
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from inbox.forms import MessageForm
from django.http import HttpResponseRedirect

@login_required
def inbox(request):
    return TemplateResponse(request, 'inbox/inbox.html', {'messages': request.user.inboxMessages.exclude(isDeleted=True)})

@login_required
def sended(request):
    return TemplateResponse(request, 'inbox/sended.html', {'messages': request.user.sendedMessages})

@login_required
def trash(request):
    return TemplateResponse(request, 'inbox/trash.html', {'messages': request.user.inboxMessages.exclude(isDeleted=False)})

@login_required
def compose(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)            
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/inbox/")
    else:
        form = MessageForm(initial={'sender': request.user})

    return TemplateResponse(request, 'inbox/compose.html', {'form': form})

