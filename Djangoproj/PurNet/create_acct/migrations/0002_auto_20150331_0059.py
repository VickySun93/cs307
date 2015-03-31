# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_acct', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='course_list',
            new_name='courses',
        ),
    ]
