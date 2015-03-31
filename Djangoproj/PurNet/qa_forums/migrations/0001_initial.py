# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_acct', '0001_initial'),
        ('course_mang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_title', models.CharField(max_length=100)),
                ('question_text', models.CharField(max_length=1000)),
                ('ques_date', models.DateTimeField(verbose_name='date published')),
                ('thread_course', models.ForeignKey(to='course_mang.Course')),
                ('thread_owner', models.ForeignKey(to='create_acct.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Forum_Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.CharField(max_length=2000)),
                ('resp_date', models.DateTimeField(verbose_name='date published')),
                ('forum_question', models.ForeignKey(to='qa_forums.Forum_Question')),
                ('response_owner', models.ForeignKey(to='create_acct.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
