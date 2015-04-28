from django.http import Http404
from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import RequestContext
from tutor.models import Entry
from django.http import HttpResponse


def entries(request):
    entries = Entry.objects.filter(status=Entry.PUBLISHED).order_by('-start_publication',)
    context = RequestContext(request, {'entries': entries})
    return render_to_response('blog/entries.html', context)

def entry(request, slug):
    try:
        blog_entry = Entry.objects.get(slug=slug, status=Entry.PUBLISHED)
    except Entry.DoesNotExist:
        raise Http404
    context = RequestContext(request, {'entry': blog_entry})
    return render_to_response('blog/entry.html', context)

def cs180(request):
    return render(request, 'cs180.html')

def cs182(request):
    return render(request, 'cs182.html')

def cs250(request):
    return render(request, 'cs250.html')

def cs251(request):
    return render(request, 'cs251.html')

def cs252(request):
    return render(request, 'cs252.html')

def cs240(request):
    return render(request, 'cs240.html')

def cs348(request):
    return render(request, 'cs348.html')