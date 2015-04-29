# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0003_auto_20150410_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': 'Messages', 'verbose_name': 'Message'},
        ),
    ]
