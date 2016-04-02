from django.conf.urls import url

from oliver_screen.api import LastTrackView, CurrentTrackView
from oliver_screen.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # API
    url(r'^api/track/last/', LastTrackView.as_view(), name='track-last'),
    url(r'^api/track/current/', CurrentTrackView.as_view(), name='track-current')
]
