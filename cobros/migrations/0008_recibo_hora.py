# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0007_recibo_presentado'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='hora',
            field=models.TimeField(default=datetime.datetime.now, null=True, editable=False, blank=True),
        ),
    ]
