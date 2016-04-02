from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OliveScreenConfig(AppConfig):
    name = 'oliver_screen'
    verbose_name = _('Oliver Screen')

    def ready(self):
        pass