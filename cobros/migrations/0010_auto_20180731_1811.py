# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0009_auto_20180716_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presentacioncobros',
            options={'verbose_name': 'Rendicion de cobros', 'verbose_name_plural': 'Rendiciones de cobros'},
        ),
        migrations.RenameField(
            model_name='presentacioncobros',
            old_name='vendedor',
            new_name='cobrador',
        ),
    ]
