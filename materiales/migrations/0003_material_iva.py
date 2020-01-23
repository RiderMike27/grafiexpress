# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_material_retiro_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='iva',
            field=models.IntegerField(default=10, choices=[(10, b'IVA 10%'), (5, b'IVA 5%'), (0, b'EXCENTA')]),
        ),
    ]
