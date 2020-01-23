# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0023_programacion_realizada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleproduccion',
            name='detalle_proceso',
        ),
        migrations.AddField(
            model_name='detalleproduccion',
            name='detalle_programacion',
            field=models.ForeignKey(default=1, to='produccion.DetalleProgramacion'),
            preserve_default=False,
        ),
    ]
