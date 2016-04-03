import json
import logging

from django.conf import settings
from huey.contrib.djhuey import db_task
from channels import Group

from oliver_screen import utils, lastfm
from oliver_screen.models import ScreenConsumer

logger = logging.getLogger(__name__)


@db_task()
def update_screens_task():
    screen_channel_group = Group(settings.OLIVER_WS_GROUP)
    logger.debug('Updating screens')

    user = lastfm.get_user()
    track = user.get_now_playing()
    if track is None:
        track_data = utils.get_current_from_cache()
        logger.debug("sending ", track_data, "to", screen_channel_group.name)
        screen_channel_group.send({'track': json.dumps({'track': track_data})})
        return

    artist = track.get_artist()
    image = artist.get_cover_image(size=4)

    track_data = {
        'artist': artist.get_name(),
        'title': track.get_title(),
        'image': image,
    }
    utils.cache_current(track_data)

    logger.debug("sending ", track_data, "to", screen_channel_group.name)
    screen_channel_group.send({'text': json.dumps({'track': track_data})})

    # At least one active screen
    if ScreenConsumer.objects.filter(is_active=True).exists():
        update_screens_task.schedule(delay=settings.OLIVER_LASTFM_POLL_INTERVAL)
    else:
        logger.debug('No active screens, bailing')

    return track_data
