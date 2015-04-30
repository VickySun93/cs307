# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0006_auto_20150428_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='', max_length=40, verbose_name='subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(default='', max_length=100, verbose_name='message'),
            preserve_default=True,
        ),
    ]
