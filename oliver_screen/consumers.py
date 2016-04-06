from channels import Group
from channels.sessions import channel_session
from django.conf import settings

from oliver_screen.tasks import update_screens_task


@channel_session
def ws_message(message):
    pass


@channel_session
def ws_connect(message):
    g = Group(settings.OLIVER_WS_GROUP, channel_layer=message.channel_layer)
    g.add(message.reply_channel)

    update_screens_task()  # async


@channel_session
def ws_disconnect(message):
    Group(settings.OLIVER_WS_GROUP, channel_layer=message.channel_layer).discard(message.reply_channel)

    # update_screens_task.revoke()
