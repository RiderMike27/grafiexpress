# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_auto_20161209_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendetrabajo',
            name='prueba_realizada',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
