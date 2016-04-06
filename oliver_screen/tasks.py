import json
import logging

from django.conf import settings
from django.core.cache import cache
from huey.contrib.djhuey import db_task
from channels import Group

from oliver_screen import lastfm

logger = logging.getLogger(__name__)

LOCK_EXPIRE = 60 * 5  # Lock expires in 5 minutes


def acquire_lock(lock_id):
    # cache.add fails if the key already exists
    return cache.add(lock_id, 'true', LOCK_EXPIRE)


def release_lock(lock_id):
    # memcache delete is very slow, but we have to use it to take advantage of using add() for atomic locking
    return cache.delete(lock_id)


@db_task()
def update_screens_task():
    screen_channel_group = Group(settings.OLIVER_WS_GROUP)
    lock_id = '{0}-lock'.format(settings.OLIVER_WS_GROUP)

    logger.debug('Updating screens')
    if acquire_lock(lock_id):
        try:
            track_data = lastfm.get_track_data()
        finally:
            release_lock(lock_id)

        screen_channel_group.send({'text': json.dumps({'track': track_data})})

        update_screens_task.schedule(delay=settings.OLIVER_LASTFM_POLL_INTERVAL)

        return track_data

    logger.debug('Last.FM is already being polled, doing nothing.')

