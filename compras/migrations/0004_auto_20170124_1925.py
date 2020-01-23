# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='fecha_de_vencimiento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateField(default=datetime.date.today, verbose_name=b'fecha de emision'),
        ),
        migrations.RemoveField(
            model_name='compra',
            name='orden_de_compra',
        ),
        migrations.AddField(
            model_name='compra',
            name='orden_de_compra',
            field=models.ManyToManyField(to='compras.OrdenDeCompra', blank=True),
        ),
        migrations.AlterField(
            model_name='ordendecompra',
            name='fecha',
            field=models.DateField(default=datetime.date.today, verbose_name=b'fecha de emision'),
        ),
    ]
