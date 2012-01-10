from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^dojango/', include('dojango.urls')),
	(r'^my-first-page/$', 'myapp.views.first_page'),
    # Examples:
    # url(r'^$', 'myproject3.views.home', name='home'),
    # url(r'^myproject3/', include('myproject3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
