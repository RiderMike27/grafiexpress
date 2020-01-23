# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20161118_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='contacto',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
