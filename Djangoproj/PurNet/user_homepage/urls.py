from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'PurNet.views.index'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^admin/', include(admin.site.urls)),
)
