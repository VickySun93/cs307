from django.conf.urls import patterns, include, url

urlpatterns =[
    url(r'^$', 'inbox.views.inbox', name="inbox"),
    url(r'^sended/$', 'inbox.views.sended', name="sended"),
    url(r'^trash/$', 'inbox.views.trash', name="trash"),
    url(r'^compose/$', 'inbox.views.compose', name="compose"),
]
