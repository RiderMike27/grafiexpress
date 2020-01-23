# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ruc',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'RUC'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=50, null=True, verbose_name=b'tel\xc3\xa9fono'),
        ),
    ]
