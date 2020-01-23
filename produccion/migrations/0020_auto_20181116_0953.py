# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0019_auto_20181115_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleprogramacion',
            name='fecha_de_finalizacion',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='detalleprogramacion',
            name='hora_de_finalizacion',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='programacion',
            name='fecha_de_entrega',
            field=models.DateField(null=True, blank=True),
        ),
    ]
