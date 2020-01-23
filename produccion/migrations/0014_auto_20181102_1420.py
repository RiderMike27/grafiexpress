# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0013_auto_20181101_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProgramacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_inicio', models.DateField()),
                ('hora_de_inicio', models.TimeField(default=datetime.time(8, 0))),
                ('pliegos', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Trabajo',
                'verbose_name_plural': 'Trabajos',
            },
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_inicio', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AlterField(
            model_name='detalleproceso',
            name='estado',
            field=models.CharField(max_length=15, editable=False, choices=[(b'no_iniciado', b'No iniciado'), (b'en_proceso', b'En proceso'), (b'finalizado', b'Finalizado')]),
        ),
        migrations.AlterField(
            model_name='maquina',
            name='tareas_en_cola',
            field=models.IntegerField(default=0, verbose_name=b'horas ocupadas', editable=False),
        ),
        migrations.AddField(
            model_name='programacion',
            name='maquina',
            field=models.ForeignKey(to='produccion.Maquina'),
        ),
        migrations.AddField(
            model_name='detalleprogramacion',
            name='detalle_proceso',
            field=models.ForeignKey(to='produccion.DetalleProceso'),
        ),
        migrations.AddField(
            model_name='detalleprogramacion',
            name='programacion',
            field=models.ForeignKey(to='produccion.Programacion'),
        ),
    ]
