# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0003_auto_20191001_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='vendedor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
