# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='isDeleted',
            field=models.BooleanField(default=False, verbose_name=b'deleted'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=100, verbose_name=b'message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name='inboxMessages', verbose_name=b'to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='sendedMessages', verbose_name=b'from', to=settings.AUTH_USER_MODEL),
        ),
    ]
