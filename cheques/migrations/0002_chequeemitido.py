# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bancos', '0001_initial'),
        ('cheques', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChequeEmitido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=100)),
                ('monto', models.DecimalField(max_digits=15, decimal_places=2)),
                ('es_diferido', models.BooleanField(default=False)),
                ('fecha_de_emision', models.DateField(default=datetime.date.today)),
                ('banco', models.ForeignKey(to='bancos.Banco')),
            ],
        ),
    ]
