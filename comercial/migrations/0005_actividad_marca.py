# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20190930_0018'),
        ('comercial', '0004_auto_20191003_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='marca',
            field=models.ForeignKey(blank=True, to='clientes.Marca', null=True),
        ),
    ]
