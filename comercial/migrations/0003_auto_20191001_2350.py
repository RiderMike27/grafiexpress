# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0002_auto_20191001_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha',
            field=models.DateField(default=datetime.datetime.today, verbose_name=b'Fecha'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='otros',
            field=models.CharField(max_length=200, verbose_name=b'especificar', blank=True),
        ),
    ]
