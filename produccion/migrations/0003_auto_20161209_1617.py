# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_auto_20161205_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleordendetrabajo',
            name='entregado',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='detalleordendetrabajo',
            name='restante',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='entregado',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='restante',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
    ]
