from django.conf.urls.defaults import patterns, include

from myproject.checkin.views import current_datetime, hours_ahead


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'myproject.checkin.views.index'),
                       (r'^pans/(?P<pan_id>\d+)/$', 'myproject.checkin.views.detail'),
                       (r'^time/$', current_datetime),
                       ('^another-time-page/$', current_datetime),
                       (r'^time/plus/(\d{1,2})/$', hours_ahead),

                       # Examples:
                       # url(r'^$', 'myproject.views.home', name='home'),
                       # url(r'^myproject/', include('myproject.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       (r'^admin/', include(admin.site.urls)),
                       (r'^admin_tools/', include('admin_tools.urls')),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media'}),

)
