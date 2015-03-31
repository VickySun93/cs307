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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=40)),
                ('courses', models.ManyToManyField(to='course_mang.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
