# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0014_auto_20181102_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleprogramacion',
            name='fecha_de_inicio',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
