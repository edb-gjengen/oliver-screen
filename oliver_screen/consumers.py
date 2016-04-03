from channels import Group
from channels.sessions import channel_session
from django.conf import settings
import json

from oliver_screen.models import ScreenConsumer
from oliver_screen.tasks import update_screens_task


@channel_session
def ws_message(message):
    pass


@channel_session
def ws_connect(message):
    g = Group(settings.OLIVER_WS_GROUP, channel_layer=message.channel_layer)
    g.add(message.reply_channel)

    active_consumers = ScreenConsumer.objects.filter(is_active=True)
    # At last one
    if active_consumers.exists():
        screen_consumer = active_consumers.first()
    else:
        screen_consumer = ScreenConsumer.objects.create()
        update_screens_task()  # async

    g.send({'text': json.dumps({'screen_consumer': {'uuid': str(screen_consumer.uuid)}})})


@channel_session
def ws_disconnect(message):
    Group(settings.OLIVER_WS_GROUP, channel_layer=message.channel_layer).discard(message.reply_channel)

    # FIXME: only set specific uuid inactive and only revoke is no more active screens
    ScreenConsumer.objects.filter(is_active=True).update(is_active=False)
    update_screens_task.revoke()
