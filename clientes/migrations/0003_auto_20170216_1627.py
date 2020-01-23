# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20161118_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='plazo_de_credito',
            field=models.CharField(help_text=b'Plazo en d\xc3\xadas.', max_length=100, null=True, blank=True),
        ),
    ]
