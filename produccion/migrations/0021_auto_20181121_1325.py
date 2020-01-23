# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0020_auto_20181116_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='urgente',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='detalleproceso',
            name='maquina',
            field=models.ForeignKey(to='produccion.Maquina', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
