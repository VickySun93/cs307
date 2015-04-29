from django.shortcuts import render, HttpResponseRedirect
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

def add (request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        school = request.POST.get('school', '')
        num = request.POST.get('number', 0)
        major = request.POST.get('major', '')
        desc = request.POST.get('desc', '')
        crn = request.POST.get('crn', '')

        a = Course(course_school=school, course_major=major, course_title=title, course_number=num, course_CRN=crn, course_desc=desc)
        a.save()
        return HttpResponseRedirect('/courses/')
    else :
        return render_to_response('course_add.html', {'schooles':MAJOR_COLLEGES, 'majors':COURSE_MAJORS})
