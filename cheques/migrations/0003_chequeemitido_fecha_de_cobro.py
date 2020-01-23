# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheques', '0002_chequeemitido'),
    ]

    operations = [
        migrations.AddField(
            model_name='chequeemitido',
            name='fecha_de_cobro',
            field=models.DateField(null=True, blank=True),
        ),
    ]
