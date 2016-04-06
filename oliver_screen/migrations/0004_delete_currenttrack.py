# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oliver_screen', '0003_auto_20160403_1343'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CurrentTrack',
        ),
    ]
