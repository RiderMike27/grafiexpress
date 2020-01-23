# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0024_auto_20181126_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleproceso',
            name='horas_por_dia',
            field=models.IntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='programacion',
            name='realizada',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
