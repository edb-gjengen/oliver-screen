from datetime import datetime
from django.shortcuts import render

from oliver_screen import utils


def index(request):
    return render(request, 'public/index.html')


def get_last_track(request):
    user = utils.get_lastfmuser()
    playedtracks = user.get_recent_tracks(limit=2)
    playback_date = datetime.strptime(playedtracks[0].playback_date, "%d %b %Y, %H:%M")
    played = {
        'artist': playedtracks[0].track.get_artist().get_name(),
        'title': playedtracks[0].track.get_title(),
        'playback_date': playback_date,
        'utcnow': datetime.utcnow()  # provide utcnow since lastfm servers are UTC
    }
    return render(request, "public/tracks.html", {'played': played})


def get_now_playing(request):
    user = utils.get_lastfmuser()
    track = user.get_now_playing()
    if track is not None:
        artist = track.get_artist()
        video = utils.get_youtubevideo(artist.get_name(), track.get_title())
        image = artist.get_cover_image(size=4)

        if "The Shins" in artist.get_name():
            image = 'http://nikolark.at.neuf.no/the_shins.jpg'

        now_playing = {
            'artist': artist.get_name(),
            'title': track.get_title(),
            'image': image,
            'video': video
        }
        utils.cache_current(now_playing)
    else:
        # No response from LastFM db?
        now_playing = utils.get_current_from_cache()

    return render(request, "public/now_playing.html", {'now_playing': now_playing})


# Mock views
def dummy_get_last_track(request):
    played = {'artist': 'The Album Leaf', 'title': 'Another Day (Revised)'}

    return render(request, "public/tracks.html", {'played': played})


def dummy_now_playing(request):
    now_playing = {
        'artist': 'The Album Leaf',
        'title': 'Over The Pond',
        'image': 'http://userserve-ak.last.fm/serve/_/2857325/The+Album+Leaf+1155442304.jpg'
    }

    return render(request, "public/now_playing.html", {'now_playing': now_playing})
