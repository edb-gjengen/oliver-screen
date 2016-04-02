from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.humanize.templatetags.humanize import naturaltime
from dateutil import parser

from oliver_screen import lastfm, utils


class LastTrackView(APIView):
    def _get_playback_date(self, playback_date_string):
        playback_date = parser.parse(playback_date_string)
        return timezone.make_aware(playback_date, timezone.UTC())  # Last.fm API is in UTC

    def _time_since(self, playback_date_string):
        playback_date = self._get_playback_date(playback_date_string)
        formatted = naturaltime(playback_date)
        formatted = formatted.replace(u'\xa0', u' ')  # remove non-breaking space (in latin1)
        return formatted

    def get(self, request, format=None):
        user = lastfm.get_user()
        playedtracks = user.get_recent_tracks(limit=2)

        track_data = {
            'artist': playedtracks[0].track.get_artist().get_name(),
            'title': playedtracks[0].track.get_title(),
            'playback_date': self._get_playback_date(playedtracks[0].playback_date),
            'time_since': self._time_since(playedtracks[0].playback_date)
        }
        return Response({'track': track_data})


class CurrentTrackView(APIView):
    def get(self, request, format=None):
        user = lastfm.get_user()
        track = user.get_now_playing()

        if track is None:
            # No response from LastFM?
            return Response({'track': utils.get_current_from_cache()})

        artist = track.get_artist()
        video = utils.get_youtubevideo(artist.get_name(), track.get_title())
        image = artist.get_cover_image(size=4)

        now_playing = {
            'artist': artist.get_name(),
            'title': track.get_title(),
            'image': image,
            'video': video
        }
        utils.cache_current(now_playing)

        return Response({'track': now_playing})
