from django.conf.urls import patterns, include, url
from django.contrib import admin
import sys
from polls import views
sys.setrecursionlimit(10000)
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import handler500, handler404
# from dajaxice.core import dajaxice_autodiscover, dajaxice_config
# dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mypro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('polls.urls')),

    # url(r'^client_details$',views.client_details, name='client_details'),  
    # url(r'^', include('apps.user_mgnt.urls')),
)
