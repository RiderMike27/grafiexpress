# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0009_papelcosto_cantidad_en_oc'),
    ]

    operations = [
        migrations.AddField(
            model_name='compuestocosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='datosdebolsacosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='otrogastocosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='plastificadocosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='posprensamaterialcosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='posprensaotroserviciocosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='posprensaserviciocosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='preprensacosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='revistacosto',
            name='cantidad_en_oc',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
