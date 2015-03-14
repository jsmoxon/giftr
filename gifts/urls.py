from django.conf.urls import patterns, url

from gifts import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add_recipient/$', views.add_recipient, name='add_recipient'),
    url(r'^create_product/$', views.create_product, name='create_product'),
    url(r'^occasion/(?P<gift_id>\d+)/$', views.occasion_page, name='occasion_page'),
    url(r'^confirm/(?P<gift_id>\d+)/(?P<gift_option_id>\d+)/$', views.occasion_gift_confirmation_page, name='confirm_gift'),
)