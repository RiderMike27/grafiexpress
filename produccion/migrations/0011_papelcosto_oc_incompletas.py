# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0010_auto_20180216_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='papelcosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
    ]
