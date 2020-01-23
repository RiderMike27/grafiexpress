# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0025_auto_20181127_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquina',
            name='tercerizado',
            field=models.BooleanField(default=False),
        ),
    ]
