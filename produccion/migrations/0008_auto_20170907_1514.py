# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0007_auto_20170428_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleordendetrabajo',
            name='cantidad_facturada',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='detalleordendetrabajo',
            name='cantidad_no_facturada',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='cantidad_facturada',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='cantidad_no_facturada',
            field=models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2),
        ),
    ]
