# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('admin_members', models.ManyToManyField(to='authy.Site_User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site_Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('group_title', models.CharField(max_length=50)),
                ('group_desc', models.CharField(max_length=1000)),
                ('group_admins', models.OneToOneField(to='group_mang.Group_Admin')),
                ('group_members', models.ManyToManyField(to='authy.Site_User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
