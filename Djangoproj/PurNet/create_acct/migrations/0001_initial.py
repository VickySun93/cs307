# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_mang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=40)),
                ('course_list', models.ManyToManyField(to='course_mang.Courses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
