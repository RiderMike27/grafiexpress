# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0004_ordendetrabajo_prueba_realizada'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordendetrabajo',
            options={'verbose_name': 'orden de trabajo', 'verbose_name_plural': '\xf3rdenes de trabajo', 'permissions': [('view_all_ots', 'Ver Todas las OTs'), ('view_fecha_solicitada', 'Ver el campo Fecha Solicitada de la OT')]},
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='anulada',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='ordendetrabajo',
            name='fecha_solicitada',
            field=models.DateField(null=True, blank=True),
        ),
    ]
