# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100, verbose_name=b'numero de registro unico del automotor')),
                ('rua_remolque', models.CharField(max_length=100, null=True, verbose_name=b'numero de registro unico del automotor de remolquetracto o semiremolque', blank=True)),
            ],
        ),
    ]
