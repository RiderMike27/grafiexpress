# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0026_maquina_tercerizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproceso',
            name='tipo',
            field=models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado'), (b'emplacado', b'Emplacado'), (b'doblado', b'Doblado'), (b'pegado', b'Pegado'), (b'cosido', b'Cosido')]),
        ),
        migrations.AlterField(
            model_name='maquina',
            name='tipo',
            field=models.CharField(max_length=20, choices=[(b'impresion', b'Impresi\xc3\xb3n'), (b'plastificado', b'Plastificado'), (b'troquel_fabricacion', b'Troquel Fabricaci\xc3\xb3n'), (b'toquelado', b'Troquelado'), (b'terminacion', b'Terminaci\xc3\xb3n'), (b'tercerizado', b'Tercerizado'), (b'empaquetado', b'Empaquetado'), (b'emplacado', b'Emplacado'), (b'doblado', b'Doblado'), (b'pegado', b'Pegado'), (b'cosido', b'Cosido')]),
        ),
    ]
