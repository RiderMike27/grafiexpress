# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_remision_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='pagado',
            field=models.DecimalField(null=True, editable=False, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='venta',
            name='saldo',
            field=models.DecimalField(null=True, editable=False, max_digits=15, decimal_places=2),
        ),
    ]
