# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depositos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalledevolucion',
            name='material',
        ),
        migrations.RemoveField(
            model_name='detalledevolucion',
            name='orden_de_trabajo',
        ),
        migrations.AddField(
            model_name='detalledevolucion',
            name='detalle_retiro',
            field=models.ForeignKey(verbose_name=b'Material', to='depositos.DetalleRetiro', null=True),
        ),
        migrations.AddField(
            model_name='devolucion',
            name='retiro',
            field=models.ForeignKey(to='depositos.Retiro', null=True),
        ),
    ]
