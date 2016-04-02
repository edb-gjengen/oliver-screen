from django.conf.urls import include, url
from django.contrib import admin

from oliver_screen import urls as oliver_screen_urls

urlpatterns = [
    url(r'', include(oliver_screen_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
