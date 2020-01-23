# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razon_social', models.CharField(max_length=100)),
                ('ruc', models.CharField(unique=True, max_length=20)),
                ('direccion', models.CharField(max_length=200, null=True, verbose_name=b'direcci\xc3\xb3n', blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, verbose_name=b'tel\xc3\xa9fono', blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name=b'e-mail', blank=True)),
                ('condicion_de_compra', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')])),
                ('plazo_de_credito', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'proveedor',
                'verbose_name_plural': 'proveedores',
            },
        ),
    ]
