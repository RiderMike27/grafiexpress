# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0008_auto_20170907_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='papelcosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
