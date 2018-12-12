# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
