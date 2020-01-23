# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0005_auto_20170216_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordendetrabajo',
            options={'verbose_name': 'orden de trabajo', 'verbose_name_plural': '\xf3rdenes de trabajo', 'permissions': [('view_all_ots', 'Ver Todas las OTs'), ('view_fecha_solicitada', 'Ver el campo Fecha Solicitada de la OT'), ('set_vendedor_ot', 'Puede cambiar el vendedor de una OT')]},
        ),
    ]
