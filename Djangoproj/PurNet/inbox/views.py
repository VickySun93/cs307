from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.template.response import TemplateResponse
from inbox.models import Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from inbox.forms import MessageForm
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def rcvd(request):
    return TemplateResponse(request, 'inbox/rcvd.html', {'message': request.user.inboxMessages.exclude(isDeleted=True)})

@login_required
def sent(request):
    return TemplateResponse(request, 'inbox/sent.html', {'message': request.user.sentMessages})

@login_required
def inbox(request):
    return TemplateResponse(request, 'inbox/inbox.html')

@login_required
def trash(request):
    return TemplateResponse(request, 'inbox/trash.html', {'message': request.user.inboxMessages.exclude(isDeleted=False)})

@login_required
def compose(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'There was a problem sending your message.  Please review your inputs and try again')
            context = RequestContext(request, {'form': form})
            return render_to_response('inbox/compose.html/', context)
        else:
            recipient = form.cleaned_data.get('recipient')
            subject = form.cleaned_data.get('subject')
            content = form.cleaned_data.get('content')
            m = Message(sender=request.user, recipient=recipient, subject=subject, content=content)
            m.save()
            messages.add_message(request, messages.SUCCESS, 'Your message was successfully sent.')
            return HttpResponseRedirect("/inbox/compose/")
    else:
        context = RequestContext(request,  {'form': MessageForm() })
        return render_to_response('inbox/compose.html/', context)



