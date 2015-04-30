from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from group_mang.models import *

# Create your views here.


def list(request):
    """
    """
    all_groups = Site_Group.objects.all()
    return render_to_response('groups.html', {'allgroups':all_groups})

def detail(request, group_id):
    """
    """
    group = Site_Group.objects.get(id=group_id)
    if request.method == 'POST':
    	if 'join' in request.POST:
    		group.group_members.add(request.user.site_user)

    		return HttpResponseRedirect("/groupdetail/" + str(group_id))

    return render(request, 'groupdetail.html', {'group':group})

