import pylast
from django.conf import settings
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime
from dateutil import parser

from oliver_screen import utils
from oliver_screen.models import LastFMUser


def get_user():
    network = pylast.LastFMNetwork(api_key=settings.LASTFM_API_KEY, api_secret=settings.LASTFM_API_SECRET)

    lastfmusers = LastFMUser.objects.filter(active=True)
    lastfm_username = lastfmusers[0].name if len(lastfmusers) == 1 else settings.LASTFM_DEFAULT_USERNAME

    return network.get_user(lastfm_username)


def _get_playback_date(playback_date_string):
    playback_date = parser.parse(playback_date_string)

    return timezone.make_aware(playback_date, timezone.UTC())  # Last.fm API is in UTC


def _time_since(playback_date_string):
    playback_date = _get_playback_date(playback_date_string)
    formatted = naturaltime(playback_date)
    formatted = formatted.replace(u'\xa0', u' ')  # remove non-breaking space (in latin1)

    return formatted


def get_last_track_data():
    user = get_user()
    playedtracks = user.get_recent_tracks(limit=2)

    track_data = {
        'artist': playedtracks[0].track.get_artist().get_name(),
        'title': playedtracks[0].track.get_title(),
        'playback_date': _get_playback_date(playedtracks[0].playback_date),
        'time_since': _time_since(playedtracks[0].playback_date)
    }
    return track_data


def get_track_data():
    user = get_user()
    track = user.get_now_playing()

    if track is None:
        return utils.get_current_from_cache()

    artist = track.get_artist()
    image = artist.get_cover_image(size=4)

    track_data = {
        'artist': artist.get_name(),
        'title': track.get_title(),
        'image': image,
    }

    utils.cache_current(track_data)

    return track_data
