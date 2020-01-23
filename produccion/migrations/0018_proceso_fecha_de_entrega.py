# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0017_detalleproceso_hora_de_finalizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='fecha_de_entrega',
            field=models.DateField(null=True, blank=True),
        ),
    ]
