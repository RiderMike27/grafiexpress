# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_remove_talonario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talonario',
            name='tipo_de_talonario',
            field=models.IntegerField(default=0, choices=[(0, b'FACTURA'), (1, b'REMISION'), (2, b'RECIBO'), (3, b'NOTA DE CREDITO')]),
        ),
    ]
