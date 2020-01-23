# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_compra'),
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalledepago',
            name='factura',
        ),
        migrations.AddField(
            model_name='detalledepago',
            name='compra',
            field=models.ForeignKey(verbose_name=b'factura', to='compras.Compra', null=True),
        ),
    ]
