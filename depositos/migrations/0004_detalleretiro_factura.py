# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_detalleventamateriales'),
        ('depositos', '0003_auto_20170202_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleretiro',
            name='factura',
            field=models.ForeignKey(blank=True, to='ventas.Venta', null=True),
        ),
    ]
