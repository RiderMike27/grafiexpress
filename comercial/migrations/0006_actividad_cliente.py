# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20190930_0018'),
        ('comercial', '0005_actividad_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=1, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
