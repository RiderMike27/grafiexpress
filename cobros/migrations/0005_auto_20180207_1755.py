# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0004_auto_20170907_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallederecibo',
            name='factura',
            field=models.ForeignKey(blank=True, to='ventas.Venta', null=True),
        ),
        migrations.AlterField(
            model_name='detallederecibo2',
            name='medio_de_pago',
            field=models.IntegerField(default=0, choices=[(0, b'Efectivo'), (1, b'Transferencia bancaria'), (2, b'Giros'), (3, b'Cheque'), (4, b'Nota de credito'), (5, b'Retencion'), (6, b'Tarjeta de debito'), (7, b'Tarjeta de credito'), (8, b'Anticipos'), (9, b'Otros')]),
        ),
    ]
