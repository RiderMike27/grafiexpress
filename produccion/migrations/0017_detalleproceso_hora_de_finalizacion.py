# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0016_auto_20181112_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleproceso',
            name='hora_de_finalizacion',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
