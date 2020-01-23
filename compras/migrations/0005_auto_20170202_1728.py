# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0001_initial'),
        ('compras', '0004_auto_20170124_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=15, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articulo', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=15, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='compra',
            name='timbrado',
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_de_vencimiento',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='detallecompra2',
            name='compra',
            field=models.ForeignKey(to='compras.Compra'),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='compra',
            field=models.ForeignKey(to='compras.Compra'),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='material',
            field=models.ForeignKey(to='materiales.Material'),
        ),
    ]
