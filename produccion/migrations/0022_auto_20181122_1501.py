# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0021_auto_20181121_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProduccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_inicio', models.DateField(default=datetime.date.today)),
                ('hora_de_inicio', models.TimeField(default=datetime.time(8, 0))),
                ('fecha_de_finalizacion', models.DateField(null=True, blank=True)),
                ('hora_de_finalizacion', models.TimeField(null=True, blank=True)),
                ('pliegos_realizados', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_creacion', models.DateField(default=datetime.date.today, editable=False)),
                ('programacion', models.ForeignKey(to='produccion.Programacion')),
            ],
        ),
        migrations.AlterField(
            model_name='detalleproceso',
            name='tipo',
            field=models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado'), (b'emplacado', b'Emplacado')]),
        ),
        migrations.AlterField(
            model_name='maquina',
            name='tipo',
            field=models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado'), (b'emplacado', b'Emplacado')]),
        ),
        migrations.AddField(
            model_name='detalleproduccion',
            name='detalle_proceso',
            field=models.ForeignKey(to='produccion.DetalleProceso'),
        ),
        migrations.AddField(
            model_name='detalleproduccion',
            name='produccion',
            field=models.ForeignKey(to='produccion.Produccion'),
        ),
    ]
