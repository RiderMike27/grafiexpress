# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import comercial.models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0007_auto_20191020_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='documentos',
            field=models.FileField(null=True, upload_to=comercial.models.get_file_path, blank=True),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='otros',
            field=models.CharField(help_text=b'especificar', max_length=200, blank=True),
        ),
    ]
