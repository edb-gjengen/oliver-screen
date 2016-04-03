from django.contrib import admin

from oliver_screen.models import LastFMUser, YouTubeVideo, ScreenConsumer


class LastFMAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class ScreenConsumerAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'is_active', 'created']

admin.site.register(LastFMUser, LastFMAdmin)
admin.site.register(YouTubeVideo, VideoAdmin)
admin.site.register(ScreenConsumer, ScreenConsumerAdmin)
