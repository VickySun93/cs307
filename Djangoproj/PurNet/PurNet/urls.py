from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'PurNet.views.index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
    url(r'^user/password/reset/done/$','django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
