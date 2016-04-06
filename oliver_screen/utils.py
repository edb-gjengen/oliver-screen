from django.core.cache import cache
from oliver_screen.models import YouTubeVideo


def get_youtubevideo(artist, title):
    videos = YouTubeVideo.objects.filter(artist=artist, title=title)
    if len(videos) != 1:
        # should only be one
        return ""

    return videos[0]

CACHE_KEY = 'oliver-track'


def cache_current(track):
    return cache.set(CACHE_KEY, track, 20)  # in seconds


def get_current_from_cache():
    return cache.get(CACHE_KEY)
