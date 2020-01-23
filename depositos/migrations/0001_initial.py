# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
        ('funcionarios', '0001_initial'),
        ('materiales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Baja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleAlta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('motivo', models.CharField(max_length=500, null=True, blank=True)),
                ('alta', models.ForeignKey(to='depositos.Alta')),
                ('material', models.ForeignKey(to='materiales.Material')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleBaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('motivo', models.CharField(max_length=500, null=True, blank=True)),
                ('baja', models.ForeignKey(to='depositos.Baja')),
                ('material', models.ForeignKey(to='materiales.Material')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleDevolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('deposito', models.ForeignKey(to='depositos.Deposito')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleRetiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('deposito', models.ForeignKey(to='depositos.Deposito')),
                ('material', models.ForeignKey(to='materiales.Material')),
                ('orden_de_trabajo', models.ForeignKey(blank=True, to='produccion.OrdenDeTrabajo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('funcionario', models.ForeignKey(to='funcionarios.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('funcionario', models.ForeignKey(to='funcionarios.Funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='detalleretiro',
            name='retiro',
            field=models.ForeignKey(to='depositos.Retiro'),
        ),
        migrations.AddField(
            model_name='detalledevolucion',
            name='devolucion',
            field=models.ForeignKey(to='depositos.Devolucion'),
        ),
        migrations.AddField(
            model_name='detalledevolucion',
            name='material',
            field=models.ForeignKey(to='materiales.Material'),
        ),
        migrations.AddField(
            model_name='detalledevolucion',
            name='orden_de_trabajo',
            field=models.ForeignKey(blank=True, to='produccion.OrdenDeTrabajo', null=True),
        ),
        migrations.AddField(
            model_name='baja',
            name='deposito',
            field=models.ForeignKey(to='depositos.Deposito'),
        ),
        migrations.AddField(
            model_name='baja',
            name='funcionario',
            field=models.ForeignKey(to='funcionarios.Funcionario'),
        ),
        migrations.AddField(
            model_name='alta',
            name='deposito',
            field=models.ForeignKey(to='depositos.Deposito'),
        ),
        migrations.AddField(
            model_name='alta',
            name='funcionario',
            field=models.ForeignKey(to='funcionarios.Funcionario'),
        ),
    ]
