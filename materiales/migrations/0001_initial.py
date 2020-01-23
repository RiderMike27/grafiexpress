# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDeMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'categor\xeda de materiales',
                'verbose_name_plural': 'categor\xedas de materiales',
            },
        ),
        migrations.CreateModel(
            name='Gramaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150, verbose_name=b'descripci\xc3\xb3n')),
                ('codigo', models.CharField(max_length=10, null=True, verbose_name=b'c\xc3\xb3digo', blank=True)),
                ('stock_actual', models.DecimalField(default=0, editable=False, max_digits=15, decimal_places=2)),
                ('costo_actual', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('retiro_ot', models.BooleanField(default=True, verbose_name=b'retiro en OT')),
                ('marca', models.CharField(max_length=100, null=True, blank=True)),
                ('categoria', models.ForeignKey(verbose_name=b'categor\xc3\xada', to='materiales.CategoriaDeMaterial')),
                ('gramaje', models.ForeignKey(blank=True, to='materiales.Gramaje', null=True)),
            ],
            options={
                'verbose_name_plural': 'materiales',
            },
        ),
        migrations.CreateModel(
            name='Resma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadDeMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('simbolo', models.CharField(max_length=10, null=True, verbose_name=b'S\xc3\xadmbolo', blank=True)),
            ],
            options={
                'verbose_name': 'unidad de medida',
                'verbose_name_plural': 'unidades de medida',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='resma',
            field=models.ForeignKey(blank=True, to='materiales.Resma', null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='unidad_de_medida',
            field=models.ForeignKey(to='materiales.UnidadDeMedida'),
        ),
    ]
