# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20161220_1519'),
        ('clientes', '0002_auto_20161118_1344'),
        ('bancos', '0001_initial'),
        ('ventas', '0005_auto_20161220_1519'),
        ('cheques', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleDeRecibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(max_digits=15, decimal_places=2)),
                ('factura', models.ForeignKey(to='ventas.Venta')),
            ],
            options={
                'verbose_name': 'Detalle de factura',
                'verbose_name_plural': 'Detalle de facturas',
            },
        ),
        migrations.CreateModel(
            name='DetalleDeRecibo2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medio_de_pago', models.IntegerField(default=0, choices=[(0, b'Efectivo'), (1, b'Transferencia bancaria'), (2, b'Giros'), (3, b'Cheque'), (4, b'Nota de credito'), (5, b'Retencion'), (6, b'Tarjeta de debito'), (7, b'Tarjeta de credito')])),
                ('numero_de_comprobante', models.CharField(max_length=100, null=True, blank=True)),
                ('monto', models.DecimalField(max_digits=15, decimal_places=2)),
                ('cheque', models.ForeignKey(blank=True, to='cheques.ChequeRecibido', null=True)),
                ('cuenta_bancaria', models.ForeignKey(blank=True, to='bancos.CuentaBancaria', null=True)),
            ],
            options={
                'verbose_name': 'Detalle de medio de pago',
                'verbose_name_plural': 'Detalle de medios de pago',
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=10)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('monto', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('talonario', models.ForeignKey(to='empresas.Talonario')),
            ],
        ),
        migrations.AddField(
            model_name='detallederecibo2',
            name='recibo',
            field=models.ForeignKey(to='cobros.Recibo'),
        ),
        migrations.AddField(
            model_name='detallederecibo',
            name='recibo',
            field=models.ForeignKey(to='cobros.Recibo'),
        ),
    ]
