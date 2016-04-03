# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oliver_screen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreenConsumer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
