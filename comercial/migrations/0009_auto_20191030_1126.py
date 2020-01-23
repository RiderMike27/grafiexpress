# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0008_auto_20191028_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialpresupuesto',
            name='precio',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
