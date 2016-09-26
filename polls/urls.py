from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
   url(r'^client_info$',views.client_info, name='client_info'),
   url(r'^client_details/(?P<id>[0-9]+)/$',views.client_details, name='client_details'),
   url(r'^client_insert$',views.client_insert, name='client_insert'),

)