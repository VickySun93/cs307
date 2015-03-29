from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()
#from django.contrib.auth.views import password_reset
#from django.conf.urls.defaults import *
#from django.contrib.auth import views
#from django.contrib.auth import views as auth_views
#from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'password.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
url(r'^admin/', include(admin.site.urls)),
                       
  url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
url(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^users/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'home.html'}),


)
