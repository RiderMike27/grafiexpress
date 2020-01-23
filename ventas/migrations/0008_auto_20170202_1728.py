# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20170124_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas', 'permissions': (('view_venta', 'Puede ver la lista de facturas'), ('print_venta', 'Puede imprimir una factura'), ('cancel_venta', 'Puede anular una factura'))},
        ),
    ]
