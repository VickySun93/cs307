from django.conf.urls import patterns, include, url

urlpatterns =[
    url(r'^signin', 'login.views.login', name="login"),
    url(r'^signout', 'login.views.logout', name="logout"),
]
