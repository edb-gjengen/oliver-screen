import pylast
from django.conf import settings
from oliver_screen.models import LastFMUser


def get_user():
    network = pylast.LastFMNetwork(api_key=settings.LASTFM_API_KEY, api_secret=settings.LASTFM_API_SECRET)
    lastfmusers = LastFMUser.objects.filter(active=True)
    if len(lastfmusers) != 1:
        # default
        return network.get_user(settings.LASTFM_DEFAULT_USERNAME)

    return network.get_user(lastfmusers[0].name)
