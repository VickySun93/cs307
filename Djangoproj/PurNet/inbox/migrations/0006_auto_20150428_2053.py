# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0005_auto_20150428_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(verbose_name='from', to=settings.AUTH_USER_MODEL, related_name='sentMessages'),
            preserve_default=True,
        ),
    ]
