# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_auto_20170103_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='fecha_de_vencimiento',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='remision',
            name='estado',
            field=models.CharField(default=b'P', max_length=1, editable=False, choices=[(b'P', b'SIN IMPRIMIR'), (b'C', b'IMPRESO'), (b'A', b'ANULADO')]),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(default=b'P', max_length=10, editable=False, choices=[(b'P', b'SIN IMPRIMIR'), (b'C', b'IMPRESO'), (b'A', b'ANULADO')]),
        ),
    ]
