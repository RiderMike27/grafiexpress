# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20161201_1245'),
        ('automoviles', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remision',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='remision',
            name='marca_del_vehiculo',
        ),
        migrations.RemoveField(
            model_name='remision',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='remision',
            name='numero_de_registro_unico_del_automotor',
        ),
        migrations.RemoveField(
            model_name='remision',
            name='numero_de_rua_de_remolquetracto_o_semiremolque',
        ),
        migrations.RemoveField(
            model_name='remision',
            name='ruc',
        ),
        migrations.AddField(
            model_name='remision',
            name='chofer',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
        migrations.AddField(
            model_name='remision',
            name='vehiculo',
            field=models.ForeignKey(blank=True, to='automoviles.Automovil', null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='remision',
            field=models.ManyToManyField(to='ventas.Remision'),
        ),
    ]
