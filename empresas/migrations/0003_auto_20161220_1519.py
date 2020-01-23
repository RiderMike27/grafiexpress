# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20161201_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talonario',
            name='codigo_de_establecimiento',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='talonario',
            name='punto_de_expedicion',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='talonario',
            name='timbrado',
            field=models.ForeignKey(blank=True, to='empresas.Timbrado', null=True),
        ),
        migrations.AlterField(
            model_name='talonario',
            name='tipo_de_talonario',
            field=models.IntegerField(default=0, choices=[(0, b'FACTURA'), (1, b'REMISION'), (2, b'RECIBO')]),
        ),
    ]
