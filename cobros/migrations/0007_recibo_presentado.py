# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0006_auto_20180210_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='presentado',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
