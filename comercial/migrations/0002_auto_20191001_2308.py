# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20190930_0018'),
        ('funcionarios', '0002_auto_20161201_1245'),
        ('comercial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.today, verbose_name=b'Fecha')),
                ('hora', models.TimeField(null=True, verbose_name=b'Hora', blank=True)),
                ('titulo', models.CharField(max_length=150, null=True, blank=True)),
                ('resumen', models.TextField(max_length=350)),
                ('realizado', models.BooleanField(default=True, help_text=b'Desmarcar cuando es una actividad programada')),
                ('documentos', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('fecha_creacion', models.DateField(default=datetime.datetime.now, verbose_name=b'Fecha de Creacion', editable=False)),
            ],
            options={
                'verbose_name_plural': 'CRM',
            },
        ),
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Canales',
            },
        ),
        migrations.AddField(
            model_name='actividad',
            name='canal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comercial.Canal', null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='contacto',
            field=models.ForeignKey(to='clientes.Contacto', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='actividad',
            name='presupuesto',
            field=models.ForeignKey(blank=True, to='comercial.Presupuesto', null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='vendedor',
            field=models.ForeignKey(to='funcionarios.Funcionario', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
