# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0015_auto_20181102_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquina',
            name='fecha_disponible',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='maquina',
            name='hora_disponible',
            field=models.TimeField(default=datetime.time(8, 0)),
        ),
        migrations.AlterField(
            model_name='detalleproceso',
            name='tipo',
            field=models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado')]),
        ),
        migrations.AlterField(
            model_name='maquina',
            name='tipo',
            field=models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado')]),
        ),
    ]
