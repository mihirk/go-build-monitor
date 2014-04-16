from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from views import configuration_page, get_builds, show_builds, poll_builds

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'buildmonitor.views.home', name='home'),
                       # url(r'^buildmonitor/', include('buildmonitor.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', configuration_page),
                       url(r'^config/$', configuration_page),
                       url(r'^getbuilds/$', get_builds),
                       url(r'^monitor/$', show_builds),
                       url(r'^buffer/$', poll_builds),
)
