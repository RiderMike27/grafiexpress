# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0006_actividad_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='vendedor',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
    ]
