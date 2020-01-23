# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_auto_20171123_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='condicion',
            field=models.CharField(default=b'CR', max_length=2, choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')]),
        ),
    ]
