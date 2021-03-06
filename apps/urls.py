from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from funfactory.monkeypatches import patch
patch()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Main app:
    (r'', include('apps.pontoon.urls')),

    # BrowserID:
    url(r'^browserid/verify/$', 'apps.pontoon.views.verify', name='browserid.verify'),

    # Logout
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
