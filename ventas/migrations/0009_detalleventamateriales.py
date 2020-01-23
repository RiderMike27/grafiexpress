# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0003_material_iva'),
        ('ventas', '0008_auto_20170202_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVentaMateriales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('iva', models.IntegerField(default=10, choices=[(10, b'IVA 10%'), (5, b'IVA 5%'), (0, b'EXCENTA')])),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=15, decimal_places=2)),
                ('material', models.ForeignKey(to='materiales.Material')),
                ('venta', models.ForeignKey(to='ventas.Venta')),
            ],
            options={
                'verbose_name': 'Detalle de Venta - Materiales',
                'verbose_name_plural': 'Detalles de Venta - Materiales',
            },
        ),
    ]
