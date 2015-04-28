from django.shortcuts import render
from django.shortcuts import render_to_response
from course_mang.models import *

# Create your views here.


def list(request):
    """
    """
    all_courses = Course.objects.all()
    return render_to_response('courses.html', {'allcourses':all_courses})

def detail(request):
    """
    """
    id = request.GET.get('id', default=0)
    course = Course.objects.get(id=id)

    return render_to_response('coursedetail.html', {'course':course})

