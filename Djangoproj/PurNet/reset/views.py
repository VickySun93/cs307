from django.shortcuts import render
from reset.forms import ChangePasswordForm
# Create your views here.
def change_password(request):
    newpassword = request.POST.get("newpassword")
    renewpasssword = request.POST.get("renewpasssword")
    username=request.user.username
    if newpassword == renewpasssword:
        if request.method == 'GET':
            form = ChangePasswordForm()
        else:
            u = User.objects.get(username__exact=username)
            u.set_password(newpassword)
            u.save()
            return redirect('/users/account')
    else:
        return redirect('/change/password/')
    return render(request,'changepassword.html', {'form': form,})
