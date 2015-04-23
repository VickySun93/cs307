from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from qa import views
from django.conf.urls import url, include
from django.contrib.auth.models import User
from qa.models import Question, Tag
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug'
     )
    class Meta:
        model = Question
        fields = ('id', 'pub_date', 'question_text', 'tags', 'views')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/questions', QuestionViewSet)

    
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'PurNet.views.index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'authy.views.signup', name='signup'),
    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
    url(r'^user/password/reset/done/$','django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^change/password/$','reset.views.change_password', name='changepassword'),
    #url(r'^', include('brainstorm.urls')), 
    #url(r'^mang_acct/', include('mang_acct.urls')),
    #url(r'^course_mang/', include('course_mang.urls')),
    #url(r'^create_acct/', include('create_acct.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^inbox/', include('inbox.urls')),
    #url(r'^pass_mang/', include('pass_mang.urls')),
    #url(r'^qa_forums/', include('qa_forums.urls')),
    #url(r'^rate_prof/', include('rate_prof.urls')),
    #url(r'^reset/', include('reset.urls')),
    #url(r'^user_homepage/', include('user_homepage.urls')),
    url(r'^$', 'PurNet.views.login', name='login'),
    url(r'^logout/', 'PurNet.views.logout', name='logout'),
    #url(r'^admin/', include(admin.site.urls)),




    #url(r'^$', views.index, name='index'),
    url(r'^q/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^answer/(?P<question_id>\d+)/$', views.answer, name='answer'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$', views.add, name='add'),
    url(r'^answer/$', views.add_answer, name='add_answer'),
    url(r'^vote/(?P<user_id>\d+)/(?P<answer_id>\d+)/(?P<question_id>\d+)/(?P<op_code>\d+)/$', views.vote, name='vote'),
    url(r'^comment/(?P<answer_id>\d+)/$', views.comment, name='comment'),
    url(r'^search/$', views.search, name='search'),
    url(r'^tag/(?P<tag>\w+)/$', views.tag, name='tag'),
    url(r'^thumb/(?P<user_id>\d+)/(?P<question_id>\d+)/(?P<op_code>\d+)/$', views.thumb, name='thumb'),

    url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='profile'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),

    url('^markdown/', include( 'django_markdown.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                       
)
