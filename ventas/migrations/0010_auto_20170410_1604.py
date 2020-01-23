# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_detalleventamateriales'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalledeventa',
            options={'verbose_name': 'Detalle de la venta', 'verbose_name_plural': 'Detalles de la venta (Sin cambios)'},
        ),
        migrations.AlterModelOptions(
            name='detalledeventa2',
            options={'verbose_name': 'Detalle de la venta', 'verbose_name_plural': 'Detalles de la venta (Con cambios)'},
        ),
    ]
