# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0005_auto_20180207_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallederecibo2',
            name='medio_de_pago',
            field=models.IntegerField(default=0, choices=[(0, b'Efectivo'), (1, b'Transferencia bancaria'), (2, b'Giros'), (3, b'Cheque'), (4, b'Nota de credito'), (5, b'Retencion'), (6, b'Tarjeta de debito'), (7, b'Tarjeta de credito'), (8, b'Anticipo'), (9, b'Otros')]),
        ),
    ]
