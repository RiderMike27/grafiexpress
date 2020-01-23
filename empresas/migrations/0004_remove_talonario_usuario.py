# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20161220_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talonario',
            name='usuario',
        ),
    ]
