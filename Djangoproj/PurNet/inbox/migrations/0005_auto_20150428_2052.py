# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0004_auto_20150428_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='sendedMessages', verbose_name='from', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
