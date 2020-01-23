# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20170216_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='limite_de_credito',
            field=models.DecimalField(default=2000000.0, null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
