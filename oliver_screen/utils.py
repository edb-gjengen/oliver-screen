from oliver_screen.models import CurrentTrack, YouTubeVideo


def get_youtubevideo(artist, title):
    videos = YouTubeVideo.objects.filter(artist=artist, title=title)
    if len(videos) != 1:
        # should only be one
        return ""

    return videos[0]


def cache_current(now_playing):
    # Fetch the one CurrentTrack entry in the db and update it with the current track.
    try:
        current = CurrentTrack.objects.get(pk=1)
    except CurrentTrack.DoesNotExist:
        # update
        current = CurrentTrack(artist="", title="", image="", retries=0)

    current.artist = now_playing['artist']
    current.title = now_playing['title']
    current.image = now_playing['image']
    current.retries = 0
    current.save()


def get_current_from_cache():
    try:
        current = CurrentTrack.objects.get(pk=1)
    except CurrentTrack.DoesNotExist:
        current = CurrentTrack(artist="", title="", image="", retries=0)
        current.save()

    now_playing = {}

    # try 3 times before clearing the cache
    if current.artist != "" and current.retries < 3:
        now_playing = {
            'artist': current.artist,
            'title': current.title,
            'image': current.image
        }

        current.retries += 1
        current.save()
    else:
        current.artist = ""
        current.title = ""
        current.image = ""
        current.save()

    return now_playing