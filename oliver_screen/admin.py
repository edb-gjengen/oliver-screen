from django.contrib import admin

from oliver_screen.models import LastFMUser, YouTubeVideo


class LastFMAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(LastFMUser, LastFMAdmin)
admin.site.register(YouTubeVideo, VideoAdmin)
