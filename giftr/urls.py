from django.conf.urls import patterns, include, url
from django.contrib import admin
from gifts.views import signup_for_account

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'giftr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'gifts.views.signup_for_account', name='signup'),
    url(r'^$', 'gifts.views.home_page', name='home_page'),
    url(r'^beta_thanks/$', 'gifts.views.beta_thanks', name='beta_thanks'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'registration/pw_reset_form.html', 'email_template_name':'registration/pw_reset_email.html'}),
    url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'registration/pw_email_sent.html'}, name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name' : 'registration/password_reset.html',  'post_reset_redirect': '/gifts/'}, name='auth_password_reset_confirm' ),
    url(r'^gifts/', include('gifts.urls')), 
    url(r'^header/', 'gifts.views.header')
)
