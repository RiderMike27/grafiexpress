# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields
import datetime
import produccion.models


class Migration(migrations.Migration):

    dependencies = [
        ('maquinaria', '0001_initial'),
        ('clientes', '0001_initial'),
        ('materiales', '0001_initial'),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoOrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=produccion.models.get_file_path)),
            ],
            options={
                'verbose_name': 'archivo',
                'verbose_name_plural': 'archivos',
            },
        ),
        migrations.CreateModel(
            name='CategoriaDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'categor\xeda de trabajos',
                'verbose_name_plural': 'categor\xedas de trabajos',
            },
        ),
        migrations.CreateModel(
            name='CompuestoCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Compuesto',
                'verbose_name_plural': 'Compuestos',
            },
        ),
        migrations.CreateModel(
            name='Costo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'PENDIENTE', max_length=10)),
            ],
            options={
                'verbose_name': 'costo',
            },
        ),
        migrations.CreateModel(
            name='DatosDeBolsaCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Dato de bolsa',
                'verbose_name_plural': 'Datos de bolsa',
            },
        ),
        migrations.CreateModel(
            name='DetalleOrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200, verbose_name=b'descripci\xc3\xb3n')),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('dimensiones_x', models.DecimalField(null=True, verbose_name=b'X', max_digits=15, decimal_places=2, blank=True)),
                ('dimensiones_y', models.DecimalField(null=True, verbose_name=b'Y', max_digits=15, decimal_places=2, blank=True)),
                ('dimensiones_z', models.DecimalField(null=True, verbose_name=b'Z', max_digits=15, decimal_places=2, blank=True)),
                ('color_seleccion_frente', models.CharField(max_length=10, null=True, verbose_name=b'frente', blank=True)),
                ('color_seleccion_dorso', models.CharField(max_length=10, null=True, verbose_name=b'dorso', blank=True)),
                ('color_pantone_frente', models.CharField(max_length=10, null=True, verbose_name=b'frente', blank=True)),
                ('color_pantone_dorso', models.CharField(max_length=10, null=True, verbose_name=b'dorso', blank=True)),
                ('observaciones', models.TextField(max_length=300, null=True, blank=True)),
                ('material', models.ForeignKey(to='materiales.Material')),
            ],
            options={
                'verbose_name': 'detalle',
                'verbose_name_plural': 'detalles',
            },
        ),
        migrations.CreateModel(
            name='OrdenDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name=b'descripcion')),
                ('presupuesto_numero', models.CharField(max_length=10, null=True, verbose_name=b'n\xc3\xbamero de presupuesto', blank=True)),
                ('presupuesto_item', models.CharField(max_length=10, null=True, verbose_name=b'\xc3\xadtem', blank=True)),
                ('fecha_de_ingreso', models.DateField(default=datetime.date.today)),
                ('fecha_solicitada', models.DateField(default=datetime.date.today)),
                ('comentarios', models.TextField(null=True, blank=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('cambios', models.BooleanField(default=False)),
                ('materiales_compuestos', models.BooleanField(default=False)),
                ('originales', models.CharField(default=b'cliente', max_length=10, choices=[(b'cliente', b'Cliente'), (b'diseno', b'Dise\xc3\xb1o')])),
                ('prueba_de_color', models.BooleanField(default=False)),
                ('muestra_de_color', models.BooleanField(default=False)),
                ('prueba_de_producto', models.BooleanField(default=False)),
                ('muestra_de_producto', models.BooleanField(default=False)),
                ('repeticion', models.BooleanField(default=False, verbose_name=b'repetici\xc3\xb3n')),
                ('buscar_sobrante', models.BooleanField(default=False)),
                ('estado', models.CharField(default=b'PENDIENTE', max_length=10)),
                ('orden_de_compra_del_cliente', models.CharField(max_length=10, null=True, blank=True)),
                ('categoria', models.ForeignKey(verbose_name=b'categor\xc3\xada', to='produccion.CategoriaDeTrabajo')),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('contacto', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'cliente', chained_field=b'cliente', blank=True, auto_choose=True, to='clientes.Contacto', null=True)),
                ('marca', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'cliente', chained_field=b'cliente', blank=True, auto_choose=True, to='clientes.Marca', null=True)),
            ],
            options={
                'verbose_name': 'orden de trabajo',
                'verbose_name_plural': '\xf3rdenes de trabajo',
            },
        ),
        migrations.CreateModel(
            name='OtroGastoCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Otro gasto',
                'verbose_name_plural': 'Otros gastos',
            },
        ),
        migrations.CreateModel(
            name='PapelCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('gramaje', models.CharField(max_length=10, null=True, blank=True)),
                ('resma', models.CharField(max_length=10, null=True, blank=True)),
                ('color', models.CharField(max_length=50, null=True, blank=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Papel',
                'verbose_name_plural': 'Papeles',
            },
        ),
        migrations.CreateModel(
            name='PlastificadoCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(verbose_name=b'cantidad (cm\xc2\xb2)', max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Plastificado',
                'verbose_name_plural': 'Plastificados',
            },
        ),
        migrations.CreateModel(
            name='PosprensaMaterialCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
            },
        ),
        migrations.CreateModel(
            name='PosprensaOtroServicioCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Otro servicio',
                'verbose_name_plural': 'Otros servicios',
            },
        ),
        migrations.CreateModel(
            name='PosprensaServicioCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='PreprensaCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
                ('maquina', models.ForeignKey(blank=True, to='maquinaria.Maquina', null=True)),
            ],
            options={
                'verbose_name': 'Pre-Prensa',
            },
        ),
        migrations.CreateModel(
            name='RevistaCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Revista',
                'verbose_name_plural': 'Revistas',
            },
        ),
        migrations.CreateModel(
            name='SubcategoriaDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(verbose_name=b'categor\xc3\xada', to='produccion.CategoriaDeTrabajo')),
            ],
            options={
                'verbose_name': 'subcategor\xeda de trabajos',
                'verbose_name_plural': 'subcategor\xedas de trabajos',
            },
        ),
        migrations.CreateModel(
            name='TroquelCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('existente', models.BooleanField(default=False)),
                ('precio', models.DecimalField(max_digits=15, decimal_places=2)),
                ('costo', models.ForeignKey(to='produccion.Costo')),
            ],
            options={
                'verbose_name': 'Troquel',
                'verbose_name_plural': 'Troqueles',
            },
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='subcategoria',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'categoria', chained_field=b'categoria', verbose_name=b'subcategor\xc3\xada', blank=True, auto_choose=True, to='produccion.SubcategoriaDeTrabajo', null=True),
        ),
        migrations.AddField(
            model_name='ordendetrabajo',
            name='vendedor',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
        migrations.AddField(
            model_name='detalleordendetrabajo',
            name='orden_de_trabajo',
            field=models.ForeignKey(to='produccion.OrdenDeTrabajo'),
        ),
        migrations.AddField(
            model_name='costo',
            name='detalle_orden_de_trabajo',
            field=models.ForeignKey(to='produccion.DetalleOrdenDeTrabajo'),
        ),
        migrations.AddField(
            model_name='costo',
            name='vendedor',
            field=models.ForeignKey(blank=True, to='funcionarios.Funcionario', null=True),
        ),
        migrations.AddField(
            model_name='compuestocosto',
            name='costo',
            field=models.ForeignKey(to='produccion.Costo'),
        ),
        migrations.AddField(
            model_name='archivoordendetrabajo',
            name='orden_de_trabajo',
            field=models.ForeignKey(to='produccion.OrdenDeTrabajo'),
        ),
    ]
