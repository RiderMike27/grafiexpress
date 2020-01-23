# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150, verbose_name=b'descripci\xc3\xb3n')),
                ('precio', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name': 'm\xe1quina',
            },
        ),
    ]
