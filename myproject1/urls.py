from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'myproject1.checkin.views.index'),
	url(r'^pans/(?P<pan_id>\d+)/$', 'myproject1.checkin.views.detail'),
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject1/', include('myproject1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^admin_tools/', include('admin_tools.urls')),
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/path/to/media'}),

)
