from django.conf.urls import patterns, url

from gifts import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add_recipient/$', views.add_recipient, name='add_recipient')
)