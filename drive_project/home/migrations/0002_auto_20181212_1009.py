# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='lastname',
        ),
    ]
