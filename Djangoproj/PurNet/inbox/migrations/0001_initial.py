# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('msg_members', models.ManyToManyField(to='authy.Site_User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inbox_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('msg_text', models.CharField(max_length=1000)),
                ('msg_orig_date', models.DateTimeField(verbose_name='date sent')),
                ('msg_subject', models.CharField(max_length=100)),
                ('msg_owner', models.ForeignKey(to='authy.Site_User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inbox_Response',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('resp_text', models.CharField(max_length=1000)),
                ('resp_date', models.DateTimeField(verbose_name='date replied')),
                ('msg_parent', models.ForeignKey(to='inbox.Inbox_Message')),
                ('resp_owner', models.ForeignKey(to='authy.Site_User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inbox_group',
            name='msg_thread',
            field=models.ForeignKey(to='inbox.Inbox_Message'),
            preserve_default=True,
        ),
    ]
