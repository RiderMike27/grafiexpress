# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0008_auto_20191028_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='estado',
            field=models.CharField(default=b'pen', max_length=3, choices=[(b'pen', b'Pendiente'), (b'pre', b'Presupuestado'), (b'env', b'Enviado al cliente')]),
        ),
    ]
