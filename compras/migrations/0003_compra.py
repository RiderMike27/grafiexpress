# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_remove_talonario_usuario'),
        ('proveedores', '0003_proveedor_contacto'),
        ('compras', '0002_auto_20161201_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_de_establecimiento', models.CharField(max_length=3, editable=False)),
                ('punto_de_expedicion', models.CharField(max_length=3, editable=False)),
                ('numero_de_factura', models.CharField(max_length=10, editable=False)),
                ('timbrado', models.CharField(max_length=10, null=True)),
                ('condicion', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')])),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('total', models.DecimalField(max_digits=15, decimal_places=2)),
                ('pagado', models.DecimalField(null=True, editable=False, max_digits=15, decimal_places=2)),
                ('saldo', models.DecimalField(null=True, editable=False, max_digits=15, decimal_places=2)),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
                ('orden_de_compra', models.ForeignKey(blank=True, to='compras.OrdenDeCompra', null=True)),
                ('proveedor', models.ForeignKey(to='proveedores.Proveedor')),
                ('sucursal', models.ForeignKey(to='empresas.Sucursal')),
            ],
        ),
    ]
