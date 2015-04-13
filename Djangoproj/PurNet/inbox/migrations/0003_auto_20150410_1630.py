# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_auto_20150408_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(verbose_name='message', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='isDeleted',
            field=models.BooleanField(verbose_name='deleted', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name='inboxMessages', verbose_name='to', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='sendedMessages', verbose_name='from', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
