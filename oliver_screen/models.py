import uuid
from django.db import models


class ScreenConsumer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)


class LastFMUser(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        if self.active:
            return self.name + ": active"
        return self.name + ": NOT active"


class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)  # FIXME: Update template
    start = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        if self.active:
            return self.artist + " - " + self.title + ": active"
        return self.artist + " - " + self.title + " : NOT active"