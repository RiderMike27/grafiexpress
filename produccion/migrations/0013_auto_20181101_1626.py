# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0012_auto_20180408_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleProceso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado'), (b'entrega', b'Entrega')])),
                ('pasadas_por_pliego', models.IntegerField(default=1)),
                ('fecha_de_inicio', models.DateField(default=datetime.date.today)),
                ('hora_de_inicio', models.TimeField(null=True, blank=True)),
                ('pliegos_a_realizar', models.IntegerField(default=0)),
                ('pliegos_realizados', models.IntegerField(default=0, editable=False)),
                ('estado', models.CharField(max_length=15, choices=[(b'no_iniciado', b'No iniciado'), (b'en_proceso', b'En proceso'), (b'finalizado', b'Finalizado')])),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('pasadas_por_hora', models.IntegerField(default=1)),
                ('tipo', models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado'), (b'entrega', b'Entrega')])),
                ('tareas_en_cola', models.IntegerField(default=0, editable=False)),
                ('activa', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'M\xe1quina',
                'verbose_name_plural': 'M\xe1quinas',
            },
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pliegos', models.IntegerField(default=1)),
                ('fecha_de_creacion', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='estado_produccion',
            field=models.CharField(default=b'no_iniciado', max_length=12, choices=[(b'no_iniciado', b'No iniciado'), (b'en_proceso', b'En proceso'), (b'finalizado', b'Finalizado')]),
        ),
        migrations.AddField(
            model_name='proceso',
            name='orden_de_trabajo',
            field=models.ForeignKey(to='produccion.OrdenDeTrabajo'),
        ),
        migrations.AddField(
            model_name='detalleproceso',
            name='maquina',
            field=models.ForeignKey(to='produccion.Maquina'),
        ),
        migrations.AddField(
            model_name='detalleproceso',
            name='proceso',
            field=models.ForeignKey(to='produccion.Proceso'),
        ),
    ]
