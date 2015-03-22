from django.conf.urls import patterns, url

from gifts import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add_recipient/$', views.add_recipient, name='add_recipient'),
    url(r'^create_product/$', views.create_product, name='create_product'),
    url(r'^occasion/(?P<gift_id>\d+)/$', views.occasion_page, name='occasion_page'),
    url(r'^confirm/(?P<gift_id>\d+)/(?P<gift_option_id>\d+)/$', views.occasion_gift_confirmation_page, name='confirm_gift'),
    url(r'^send_occasion_email/(?P<user_id>\d+)/(?P<gift_id>\d+)/$', views.send_occasion_email, name='send_occasion_email'),
    url(r'^demo/$', views.demo_add_recipient, name='demo'),
    url(r'^demo_options/(?P<gift_id>\d+)/$', views.demo_options, name='demo_options')
)