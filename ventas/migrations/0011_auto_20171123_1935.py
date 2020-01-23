# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_auto_20170410_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remision',
            options={'verbose_name': 'Remision', 'verbose_name_plural': 'Remisiones', 'permissions': (('view_remision', 'Puede ver la lista de remisiones'), ('print_remision', 'Puede imprimir una remision'), ('cancel_remision', 'Puede anular una remision'))},
        ),
    ]
