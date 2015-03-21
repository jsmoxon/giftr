from django.conf.urls import patterns, url

from feedback import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)