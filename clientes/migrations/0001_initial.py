# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('ciudades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razon_social', models.CharField(max_length=100, verbose_name=b'raz\xc3\xb3n social')),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('ruc', models.CharField(unique=True, max_length=10, verbose_name=b'RUC')),
                ('direccion', models.CharField(max_length=200, null=True, verbose_name=b'direcci\xc3\xb3n')),
                ('telefono', models.CharField(max_length=20, null=True, verbose_name=b'tel\xc3\xa9fono')),
                ('email', models.CharField(max_length=100, null=True, verbose_name=b'e-mail', blank=True)),
                ('condicion_de_venta', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')])),
                ('plazo_de_credito', models.CharField(max_length=100, null=True, blank=True)),
                ('limite_de_credito', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('libre_de_impuesto', models.BooleanField(default=False, verbose_name=b'\xc2\xbfEs excento de impuesto?')),
                ('requiere_orden_de_compra_del_proveedor', models.BooleanField(default=False)),
                ('requiere_orden_de_trabajo', models.BooleanField(default=False)),
                ('requiere_numero_de_recepcion', models.BooleanField(default=False)),
                ('ciudad', models.ForeignKey(blank=True, to='ciudades.Ciudad', null=True)),
                ('vendedor', models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20, null=True, verbose_name=b'tel\xc3\xa9fono', blank=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
        ),
    ]
