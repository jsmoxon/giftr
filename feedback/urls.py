from django.conf.urls import patterns, url
from feedback import views

urlpatterns = patterns('',
    # ex: /feedback/
    url(r'^$', views.index, name='index'),
    # ex: /feedback/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /feedback/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /feedback/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)