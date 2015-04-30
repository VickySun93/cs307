from django.conf.urls import patterns, include, url

urlpatterns =[
    url(r'^$', 'inbox.views.inbox', name="inbox"),
    url(r'^sent/$', 'inbox.views.sent', name="sent"),
    url(r'^trash/$', 'inbox.views.trash', name="trash"),
    url(r'^compose/$', 'inbox.views.compose', name="compose"),
    url(r'^inbox/$', 'inbox.views.rcvd', name="inbox"),

]
