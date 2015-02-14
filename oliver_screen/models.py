from django.db import models


class CurrentTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    retries = models.IntegerField()

    def __unicode__(self):
        return self.title + " - " + self.artist


class LastFMUser(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        if self.active:
            return self.name + ": active"
        return self.name + ": NOT active"


class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)  # FIXME: Update template
    start = models.IntegerField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        if self.active:
            return self.artist + " - " + self.title + ": active"
        return self.artist + " - " + self.title + " : NOT active"