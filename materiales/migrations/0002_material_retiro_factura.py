# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='retiro_factura',
            field=models.BooleanField(default=False, verbose_name=b'retiro en Factura'),
        ),
    ]
