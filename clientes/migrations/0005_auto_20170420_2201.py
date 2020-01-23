# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20170420_2154'),
    ]

    operations = [
	migrations.RunSQL('''
         UPDATE clientes_cliente SET limite_de_credito = 2000000.00 WHERE limite_de_credito is NULL ;
        ''')
    ]
