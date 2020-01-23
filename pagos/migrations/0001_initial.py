# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bancos', '0001_initial'),
        ('proveedores', '0003_proveedor_contacto'),
        ('cheques', '0002_chequeemitido'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleDePago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factura', models.CharField(max_length=20)),
                ('monto', models.DecimalField(max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Detalle de factura',
                'verbose_name_plural': 'Detalle de facturas',
            },
        ),
        migrations.CreateModel(
            name='DetalleDePago2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medio_de_pago', models.IntegerField(default=0, choices=[(0, b'Efectivo'), (1, b'Transferencia bancaria'), (2, b'Giros'), (3, b'Cheque'), (4, b'Nota de credito'), (5, b'Retencion'), (6, b'Tarjeta de debito'), (7, b'Tarjeta de credito')])),
                ('numero_de_comprobante', models.CharField(max_length=100, null=True, blank=True)),
                ('monto', models.DecimalField(max_digits=15, decimal_places=2)),
                ('cheque', models.ForeignKey(blank=True, to='cheques.ChequeEmitido', null=True)),
                ('cuenta_bancaria', models.ForeignKey(blank=True, to='bancos.CuentaBancaria', null=True)),
            ],
            options={
                'verbose_name': 'Detalle de medio de pago',
                'verbose_name_plural': 'Detalle de medios de pago',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('monto', models.DecimalField(max_digits=15, decimal_places=2)),
                ('proveedor', models.ForeignKey(to='proveedores.Proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='detalledepago2',
            name='pago',
            field=models.ForeignKey(to='pagos.Pago'),
        ),
        migrations.AddField(
            model_name='detalledepago',
            name='pago',
            field=models.ForeignKey(to='pagos.Pago'),
        ),
    ]
