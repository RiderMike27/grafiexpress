# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0011_papelcosto_oc_incompletas'),
    ]

    operations = [
        migrations.AddField(
            model_name='compuestocosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='datosdebolsacosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='otrogastocosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plastificadocosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='posprensamaterialcosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='posprensaotroserviciocosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='posprensaserviciocosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='preprensacosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='revistacosto',
            name='oc_incompletas',
            field=models.BooleanField(default=True),
        ),
    ]
