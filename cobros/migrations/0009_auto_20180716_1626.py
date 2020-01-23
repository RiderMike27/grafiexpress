# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20161201_1245'),
        ('cobros', '0008_recibo_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePresentacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtotal', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('cobro', models.ForeignKey(to='cobros.Recibo')),
            ],
            options={
                'verbose_name': 'Cobro de presentacion',
                'verbose_name_plural': 'Cobros de presentacion',
            },
        ),
        migrations.CreateModel(
            name='PresentacionCobros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('total', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('vendedor', models.ForeignKey(to='funcionarios.Funcionario')),
            ],
            options={
                'verbose_name': 'Presentacion de cobros',
                'verbose_name_plural': 'Presentaciones de cobros',
            },
        ),
        migrations.AddField(
            model_name='detallepresentacion',
            name='presentacion',
            field=models.ForeignKey(to='cobros.PresentacionCobros'),
        ),
    ]
