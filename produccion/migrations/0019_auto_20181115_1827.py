# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0018_proceso_fecha_de_entrega'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maquina',
            name='tareas_en_cola',
        ),
        migrations.AddField(
            model_name='detalleproceso',
            name='fecha_de_finalizacion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
