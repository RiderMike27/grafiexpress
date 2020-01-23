# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0001_initial'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsumoOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='materiales.Material')),
            ],
            options={
                'verbose_name': 'Compra de insumo',
                'verbose_name_plural': 'Compras de insumos',
            },
        ),
        migrations.AlterField(
            model_name='ordendecompra',
            name='condicion',
            field=models.CharField(default=b'CO', max_length=10, choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')]),
        ),
        migrations.AddField(
            model_name='insumoordendecompra',
            name='orden_de_compra',
            field=models.ForeignKey(to='compras.OrdenDeCompra'),
        ),
    ]
