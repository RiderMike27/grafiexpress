# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0022_auto_20181122_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacion',
            name='realizada',
            field=models.BooleanField(default=False),
        ),
    ]
