# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20161205_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='remision',
            name='estado',
            field=models.CharField(default=b'P', max_length=1, editable=False),
        ),
    ]
