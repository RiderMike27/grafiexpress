# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depositos', '0002_auto_20161123_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alta',
            name='funcionario',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
        migrations.AlterField(
            model_name='baja',
            name='funcionario',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='funcionario',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
        migrations.AlterField(
            model_name='retiro',
            name='funcionario',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
    ]
