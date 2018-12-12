# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181212_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32),
        ),
    ]
