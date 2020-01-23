# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompuestoOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.CompuestoCosto')),
            ],
            options={
                'verbose_name': 'Compuesto',
                'verbose_name_plural': 'Compuestos',
            },
        ),
        migrations.CreateModel(
            name='DatosDeBolsaOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.DatosDeBolsaCosto')),
            ],
            options={
                'verbose_name': 'Dato de bolsa',
                'verbose_name_plural': 'Datos de bolsa',
            },
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('contacto', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('forma_de_pago', models.CharField(max_length=50, null=True, blank=True)),
                ('condicion', models.CharField(default=b'CONTADO', max_length=10, choices=[(b'CONTADO', b'CONTADO'), (b'CREDITO', b'CREDITO')])),
                ('cheque_diferido', models.CharField(max_length=50, null=True, blank=True)),
                ('plazo', models.CharField(max_length=50, null=True, blank=True)),
                ('departamento_solicitante', models.CharField(max_length=50, null=True, blank=True)),
                ('categoria_de_gastos', models.CharField(max_length=50, null=True, blank=True)),
                ('responsable', models.CharField(max_length=50, null=True, blank=True)),
                ('proveedor', models.ForeignKey(verbose_name=b'proveedor', to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name': 'orden de compra',
                'verbose_name_plural': 'ordenes de compra',
            },
        ),
        migrations.CreateModel(
            name='OtroGastoOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.OtroGastoCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Otro gasto',
                'verbose_name_plural': 'Otros gastos',
            },
        ),
        migrations.CreateModel(
            name='PapelOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.PapelCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Papel',
                'verbose_name_plural': 'Papeles',
            },
        ),
        migrations.CreateModel(
            name='PlastificadoOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.PlastificadoCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Plastificado',
                'verbose_name_plural': 'Plastificados',
            },
        ),
        migrations.CreateModel(
            name='PosprensaMaterialOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.PosprensaMaterialCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
            },
        ),
        migrations.CreateModel(
            name='PosprensaOtroServicioOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.PosprensaOtroServicioCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Otro servicio',
                'verbose_name_plural': 'Otros servicios',
            },
        ),
        migrations.CreateModel(
            name='PosprensaServicioOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.PosprensaServicioCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='PreprensaOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.PreprensaCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Pre-Prensa',
            },
        ),
        migrations.CreateModel(
            name='RevistaOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.RevistaCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Revista',
                'verbose_name_plural': 'Revistas',
            },
        ),
        migrations.CreateModel(
            name='TroquelOrdenDeCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='produccion.TroquelCosto')),
                ('orden_de_compra', models.ForeignKey(to='compras.OrdenDeCompra')),
            ],
            options={
                'verbose_name': 'Troquel',
                'verbose_name_plural': 'Troqueles',
            },
        ),
        migrations.AddField(
            model_name='datosdebolsaordendecompra',
            name='orden_de_compra',
            field=models.ForeignKey(to='compras.OrdenDeCompra'),
        ),
        migrations.AddField(
            model_name='compuestoordendecompra',
            name='orden_de_compra',
            field=models.ForeignKey(to='compras.OrdenDeCompra'),
        ),
    ]
