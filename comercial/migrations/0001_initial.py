# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import comercial.models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20190930_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='CantidadPresupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaterialPresupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=80, verbose_name=b'Material')),
                ('precio', models.DecimalField(max_digits=15, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora_creacion', models.DateField(verbose_name=b'Fecha de Creacion', null=True, editable=False, blank=True)),
                ('estado', models.CharField(default=b'bor', max_length=3, choices=[(b'bor', b'Borrador'), (b'pre', b'Presupuestado'), (b'env', b'Enviado al cliente')])),
                ('trabajo', models.CharField(max_length=200)),
                ('repeticion', models.BooleanField(default=False)),
                ('cambios', models.BooleanField(default=False)),
                ('corte_final', models.CharField(max_length=200, blank=True)),
                ('dimensiones_x', models.DecimalField(null=True, verbose_name=b'X', max_digits=15, decimal_places=2, blank=True)),
                ('dimensiones_y', models.DecimalField(null=True, verbose_name=b'Y', max_digits=15, decimal_places=2, blank=True)),
                ('dimensiones_z', models.DecimalField(null=True, verbose_name=b'Z', max_digits=15, decimal_places=2, blank=True)),
                ('color_seleccion_frente', models.CharField(max_length=10, null=True, verbose_name=b'frente', blank=True)),
                ('color_seleccion_dorso', models.CharField(max_length=10, null=True, verbose_name=b'dorso', blank=True)),
                ('color_pantone_frente', models.CharField(max_length=10, null=True, verbose_name=b'frente', blank=True)),
                ('color_pantone_dorso', models.CharField(max_length=10, null=True, verbose_name=b'dorso', blank=True)),
                ('terminacion', models.CharField(max_length=200, blank=True)),
                ('troquelado', models.BooleanField(default=False)),
                ('hojalado', models.BooleanField(default=False)),
                ('despuntado', models.BooleanField(default=False)),
                ('plastificado', models.BooleanField(default=False)),
                ('ambas_caras', models.BooleanField(default=False)),
                ('rel_fuego', models.BooleanField(default=False)),
                ('numerado', models.BooleanField(default=False)),
                ('otros', models.CharField(max_length=200, verbose_name=b'especificar')),
                ('observaciones', models.TextField(max_length=400, null=True, blank=True)),
                ('adjunto', models.FileField(null=True, upload_to=comercial.models.get_file_path, blank=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente', on_delete=django.db.models.deletion.PROTECT)),
                ('contacto', models.ForeignKey(to='clientes.Contacto', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Presupuestos',
            },
        ),
        migrations.AddField(
            model_name='materialpresupuesto',
            name='presupuesto',
            field=models.ForeignKey(to='comercial.Presupuesto'),
        ),
        migrations.AddField(
            model_name='cantidadpresupuesto',
            name='presupuesto',
            field=models.ForeignKey(to='comercial.Presupuesto'),
        ),
    ]
