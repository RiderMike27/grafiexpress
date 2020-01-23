# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20161201_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemisionAntiguo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('ventas.remision',),
        ),
        migrations.CreateModel(
            name='VentaAntiguo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('ventas.venta',),
        ),
        migrations.AlterField(
            model_name='venta',
            name='codigo_de_establecimiento',
            field=models.CharField(max_length=3, editable=False),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(default=b'P', max_length=10, editable=False, choices=[(b'P', b'PENDIENTE'), (b'C', b'CONFIRMADO'), (b'A', b'ANULADO')]),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_de_anulacion',
            field=models.DateField(null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='numero_de_factura',
            field=models.CharField(max_length=10, editable=False),
        ),
        migrations.AlterField(
            model_name='venta',
            name='punto_de_expedicion',
            field=models.CharField(max_length=3, editable=False),
        ),
        migrations.AlterField(
            model_name='venta',
            name='remision',
            field=models.ManyToManyField(to='ventas.Remision', blank=True),
        ),
    ]
