# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
        ('empresas', '0001_initial'),
        ('clientes', '0001_initial'),
        ('materiales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaRemision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'ventas_venta_remision',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleDeRemision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('orden_de_trabajo', models.ForeignKey(to='produccion.OrdenDeTrabajo')),
            ],
            options={
                'verbose_name': 'Detalle de la remision (OT sin cambio)',
                'verbose_name_plural': 'Detalles de la remision (OT sin cambio)',
            },
        ),
        migrations.CreateModel(
            name='DetalleDeRemision2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('detalle_orden_de_trabajo', models.ForeignKey(to='produccion.DetalleOrdenDeTrabajo')),
            ],
            options={
                'verbose_name': 'Detalle de la remision (OT con cambio)',
                'verbose_name_plural': 'Detalles de la remision (OT con cambio)',
            },
        ),
        migrations.CreateModel(
            name='DetalleDeVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('descripcion_extra', models.CharField(max_length=200, null=True, verbose_name=b'N\xc2\xba de oc/recepcion', blank=True)),
                ('iva', models.IntegerField(default=10, choices=[(10, b'IVA 10%'), (5, b'IVA 5%'), (0, b'EXCENTA')])),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=15, decimal_places=2)),
                ('orden_de_trabajo', models.ForeignKey(to='produccion.OrdenDeTrabajo')),
            ],
            options={
                'verbose_name': 'Detalle de la venta',
                'verbose_name_plural': 'Detalles de la venta',
            },
        ),
        migrations.CreateModel(
            name='DetalleDeVenta2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('descripcion_extra', models.CharField(max_length=200, null=True, verbose_name=b'N\xc2\xba de oc/recepcion', blank=True)),
                ('iva', models.IntegerField(default=10, choices=[(10, b'IVA 10%'), (5, b'IVA 5%'), (0, b'EXCENTA')])),
                ('cantidad', models.DecimalField(max_digits=15, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=15, decimal_places=2)),
                ('subtotal', models.DecimalField(max_digits=15, decimal_places=2)),
                ('detalle_orden_de_trabajo', models.ForeignKey(to='produccion.DetalleOrdenDeTrabajo')),
            ],
            options={
                'verbose_name': 'Detalle de la venta',
                'verbose_name_plural': 'Detalles de la venta',
            },
        ),
        migrations.CreateModel(
            name='Remision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_de_establecimiento', models.CharField(max_length=3, null=True)),
                ('punto_de_expedicion', models.CharField(max_length=3, null=True)),
                ('numero_de_remision', models.CharField(max_length=10, null=True)),
                ('timbrado', models.CharField(max_length=10, null=True)),
                ('fecha_de_emision', models.DateField(default=datetime.date.today)),
                ('motivo_del_traslado', models.CharField(max_length=100, null=True, blank=True)),
                ('comprobante_de_venta', models.CharField(max_length=100, null=True, blank=True)),
                ('numero_de_comprobante_de_venta', models.CharField(max_length=100, null=True, blank=True)),
                ('numero_de_timbrado', models.CharField(max_length=100, null=True, blank=True)),
                ('fecha_de_expedicion', models.DateField(default=datetime.date.today, null=True, blank=True)),
                ('fecha_de_inicio_del_traslado', models.DateField(default=datetime.date.today, null=True, blank=True)),
                ('fecha_estimada_de_termino_del_traslado', models.DateField(default=datetime.date.today, null=True, blank=True)),
                ('direccion_del_punto_de_partida', models.CharField(max_length=200, null=True, blank=True)),
                ('ciudad_de_partida', models.CharField(max_length=100, null=True, blank=True)),
                ('departamento_de_partida', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion_del_punto_de_llegada', models.CharField(max_length=200, null=True, blank=True)),
                ('ciudad_de_llegada', models.CharField(max_length=100, null=True, blank=True)),
                ('departamento_de_llegada', models.CharField(max_length=100, null=True, blank=True)),
                ('kilometros_estimados_de_recorrido', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('cambio_de_fecha_de_termino_del_traslado_o_punto_de_llegada', models.CharField(max_length=100, null=True, blank=True)),
                ('motivo', models.CharField(max_length=100, null=True, blank=True)),
                ('marca_del_vehiculo', models.CharField(max_length=100, null=True)),
                ('numero_de_registro_unico_del_automotor', models.CharField(max_length=100, null=True, blank=True)),
                ('numero_de_rua_de_remolquetracto_o_semiremolque', models.CharField(max_length=100, null=True, verbose_name=b'numero de registro unico del automotor de remolquetracto o semiremolque', blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name=b'nombre y apellido o razon social', blank=True)),
                ('ruc', models.CharField(max_length=100, null=True, verbose_name=b'RUC/CI', blank=True)),
                ('domicilio', models.CharField(max_length=100, null=True, blank=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
                ('sucursal', models.ForeignKey(to='empresas.Sucursal', null=True)),
                ('talonario', models.ForeignKey(to='empresas.Talonario', null=True)),
            ],
            options={
                'verbose_name': 'Remision',
                'verbose_name_plural': 'Remisiones',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_de_establecimiento', models.CharField(max_length=3)),
                ('punto_de_expedicion', models.CharField(max_length=3)),
                ('numero_de_factura', models.CharField(max_length=10)),
                ('timbrado', models.CharField(max_length=10, null=True)),
                ('condicion', models.CharField(default=b'CO', max_length=2, choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')])),
                ('cantidad_de_cuotas', models.IntegerField(default=0)),
                ('fecha_de_emision', models.DateField(default=datetime.date.today)),
                ('fecha_de_anulacion', models.DateField(null=True, blank=True)),
                ('estado', models.CharField(default=b'P', max_length=10, choices=[(b'P', b'PENDIENTE'), (b'C', b'CONFIRMADO'), (b'A', b'ANULADO')])),
                ('total', models.DecimalField(max_digits=15, decimal_places=2)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
                ('remision', models.ManyToManyField(to='ventas.Remision', null=True, blank=True)),
                ('sucursal', models.ForeignKey(to='empresas.Sucursal', null=True)),
                ('talonario', models.ForeignKey(to='empresas.Talonario', null=True)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'permissions': (('print_venta', 'Puede imprimir una factura'), ('cancel_venta', 'Puede anular una factura')),
            },
        ),
        migrations.AddField(
            model_name='detalledeventa2',
            name='venta',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
        migrations.AddField(
            model_name='detalledeventa',
            name='venta',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
        migrations.AddField(
            model_name='detallederemision2',
            name='remision',
            field=models.ForeignKey(to='ventas.Remision'),
        ),
        migrations.AddField(
            model_name='detallederemision2',
            name='unidad_de_medida',
            field=models.ForeignKey(blank=True, to='materiales.UnidadDeMedida', null=True),
        ),
        migrations.AddField(
            model_name='detallederemision',
            name='remision',
            field=models.ForeignKey(to='ventas.Remision'),
        ),
        migrations.AddField(
            model_name='detallederemision',
            name='unidad_de_medida',
            field=models.ForeignKey(blank=True, to='materiales.UnidadDeMedida', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='venta',
            unique_together=set([('codigo_de_establecimiento', 'punto_de_expedicion', 'numero_de_factura', 'timbrado')]),
        ),
        migrations.AlterUniqueTogether(
            name='remision',
            unique_together=set([('codigo_de_establecimiento', 'punto_de_expedicion', 'numero_de_remision', 'timbrado')]),
        ),
    ]
