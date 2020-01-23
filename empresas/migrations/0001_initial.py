# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('ruc', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=200, null=True, verbose_name=b'direcci\xc3\xb3n', blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, verbose_name=b'tel\xc3\xa9fono', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name=b'e-mail', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200, null=True, verbose_name=b'direcci\xc3\xb3n', blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, verbose_name=b'tel\xc3\xa9fono', blank=True)),
                ('email', models.CharField(max_length=100, null=True, verbose_name=b'e-mail', blank=True)),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
            ],
            options={
                'verbose_name': 'sucursal',
                'verbose_name_plural': 'sucursales',
            },
        ),
        migrations.CreateModel(
            name='Talonario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('tipo_de_talonario', models.IntegerField(default=0, choices=[(0, b'FACTURA'), (1, b'REMISION')])),
                ('fecha_de_caducidad', models.DateField(null=True, blank=True)),
                ('fecha_de_creacion', models.DateField(default=datetime.date.today)),
                ('numero_inicial', models.IntegerField()),
                ('numero_final', models.IntegerField()),
                ('ultimo_usado', models.IntegerField(null=True, blank=True)),
                ('codigo_de_establecimiento', models.CharField(max_length=3)),
                ('punto_de_expedicion', models.CharField(max_length=3)),
                ('agotado', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=False)),
                ('sucursal', models.ForeignKey(to='empresas.Sucursal', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timbrado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=10)),
                ('fecha_de_inicio', models.DateField(null=True)),
                ('fecha_de_vencimiento', models.DateField(null=True)),
                ('activo', models.BooleanField(default=True)),
                ('empresa', models.ForeignKey(to='empresas.Empresa', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='talonario',
            name='timbrado',
            field=models.ForeignKey(to='empresas.Timbrado', null=True),
        ),
        migrations.AddField(
            model_name='talonario',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
