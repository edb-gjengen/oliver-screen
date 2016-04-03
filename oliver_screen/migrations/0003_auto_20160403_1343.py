# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oliver_screen', '0002_screenconsumer'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenconsumer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 3, 11, 43, 17, 217624, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenconsumer',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 3, 11, 43, 26, 177296, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
