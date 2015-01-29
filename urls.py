from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qpcmms.views',
    # Examples:
    # url(r'^$', 'qpcm.views.home', name='home'),
    # url(r'^qpcm/', include('qpcm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'index'),
    url(r'^members/', 'members'),
    url(r'^users/', 'users'),
    url(r'^common/', 'common'),
   
)
