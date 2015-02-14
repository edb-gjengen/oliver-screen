from django.conf.urls import patterns, url

urlpatterns = patterns(
    'oliver_screen.views',
    url(r'^last/$', 'get_last_track', name='last-track'),
    url(r'^now_playing/$', 'get_now_playing', name='now-playing'),
)