# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181212_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=32),
        ),
    ]
