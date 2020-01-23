# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0002_auto_20170103_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallederecibo',
            options={'verbose_name': 'Detalle de cobro (Facturas)', 'verbose_name_plural': 'Detalle de cobro (Facturas)'},
        ),
        migrations.AlterModelOptions(
            name='detallederecibo2',
            options={'verbose_name': 'Detalle de cobro (Medio de pago)', 'verbose_name_plural': 'Detalle de cobro (Medios de pago)'},
        ),
    ]
