from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'oliver_screen.views.index', name='index'),
    url(r'', include('oliver_screen.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
