# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0003_auto_20170216_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallederecibo',
            options={'verbose_name': 'Factura', 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterModelOptions(
            name='detallederecibo2',
            options={'verbose_name': 'Medio de pago', 'verbose_name_plural': 'Medios de pago'},
        ),
    ]
