# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20161220_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remision',
            options={'verbose_name': 'Remision', 'verbose_name_plural': 'Remisiones', 'permissions': (('print_remision', 'Puede imprimir una remision'), ('cancel_remision', 'Puede anular una remision'))},
        ),
    ]
