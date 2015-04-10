# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100, verbose_name=b'mensaje')),
                ('recipient', models.ForeignKey(related_name='inboxMessages', verbose_name=b'para', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sendedMessages', verbose_name=b'de', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
    ]
