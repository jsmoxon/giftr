from django.conf.urls import patterns, include, url
from django.contrib import admin
from gifts.views import signup_for_account

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'giftr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'gifts.views.signup_for_account', name='signup'),
#not sure that login function is doing anything in the line below. Shoudl it be removed? Is it harmful?
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'home_page.html'}, name='home_page'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^gifts/', include('gifts.urls')), 
)
