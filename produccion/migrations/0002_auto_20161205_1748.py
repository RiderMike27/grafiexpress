# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendetrabajo',
            name='estado',
            field=models.CharField(default=b'PENDIENTE', max_length=10, editable=False),
        ),
    ]
