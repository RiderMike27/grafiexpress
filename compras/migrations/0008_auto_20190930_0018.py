# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_auto_20170708_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallecompra2',
            options={'verbose_name': 'Insumo compra', 'verbose_name_plural': 'Insumos compra'},
        ),
        migrations.AlterField(
            model_name='compra',
            name='condicion',
            field=models.CharField(default=b'CR', max_length=2, choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')]),
        ),
    ]
