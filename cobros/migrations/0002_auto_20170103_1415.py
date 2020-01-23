# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recibo',
            options={'permissions': (('print_recibo', 'Puede imprimir un recibo'), ('cancel_recibo', 'Puede anular un recibo'))},
        ),
        migrations.AddField(
            model_name='recibo',
            name='estado',
            field=models.IntegerField(default=0, editable=False, choices=[(0, b'NO IMPRESO'), (1, b'IMPRESO'), (2, b'ANULADO')]),
        ),
    ]
