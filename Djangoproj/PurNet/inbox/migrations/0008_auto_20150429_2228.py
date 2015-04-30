# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0007_auto_20150428_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=300, verbose_name='message', default=''),
            preserve_default=True,
        ),
    ]
