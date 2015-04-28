# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('tutor.views',
    url(r'^$', 'entries', name='entries'),
    url(r'^(?P<slug>[-\w]+)/$', 'entry', name='entry'),
    url(r'^blog/cs180\.html$', 'cs180', name='cs180'),
)