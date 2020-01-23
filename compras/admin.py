from __future__ import print_function
from django.contrib import admin
from django.contrib.admin.decorators import register
from compras.models import *
from compras.forms import *


class PapelOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = PapelOrdenDeCompra
    form = PapelOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class PreprensaOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = PreprensaOrdenDeCompra
    form = PreprensaOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class TroquelOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = TroquelOrdenDeCompra
    form = TroquelOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class PosprensaServicioOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = PosprensaServicioOrdenDeCompra
    form = PosprensaServicioOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class PosprensaMaterialOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = PosprensaMaterialOrdenDeCompra
    form = PosprensaMaterialOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class PosprensaOtroServicioOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = PosprensaOtroServicioOrdenDeCompra
    form = PosprensaOtroServicioOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class DatosDeBolsaOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = DatosDeBolsaOrdenDeCompra
    form = DatosDeBolsaOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class RevistaOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = RevistaOrdenDeCompra
    form = RevistaOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class CompuestoOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = CompuestoOrdenDeCompra
    form = CompuestoOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class PlastificadoOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = PlastificadoOrdenDeCompra
    form = PlastificadoOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class OtroGastoOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = OtroGastoOrdenDeCompra
    form = OtroGastoOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_tabular.html'


class InsumoOrdenDeCompraInlineAdmin(admin.TabularInline):
    model = InsumoOrdenDeCompra
    form = InsumoOrdenDeCompraForm
    extra = 1
    fieldsets = ((None,{ 'fields': [ 'descripcion', 'cantidad', 'precio_unitario', 'subtotal'] }),)
    template = 'ordendecompra_insumo_tabular.html'


@register(OrdenDeCompra)
class OrdenDeCompraAdmin(admin.ModelAdmin):
    form = OrdenDeCompraForm

    change_form_template = 'ordendecompra_form.html'
    inlines = [
        PapelOrdenDeCompraInlineAdmin,
        PreprensaOrdenDeCompraInlineAdmin,
        TroquelOrdenDeCompraInlineAdmin,
        PosprensaServicioOrdenDeCompraInlineAdmin,
        PosprensaMaterialOrdenDeCompraInlineAdmin,
        PosprensaOtroServicioOrdenDeCompraInlineAdmin,
        DatosDeBolsaOrdenDeCompraInlineAdmin,
        RevistaOrdenDeCompraInlineAdmin,
        CompuestoOrdenDeCompraInlineAdmin,
        PlastificadoOrdenDeCompraInlineAdmin,
        OtroGastoOrdenDeCompraInlineAdmin,
        InsumoOrdenDeCompraInlineAdmin,
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creado_por = request.user
        obj.save()


class DetalleCompraInlineAdmin(admin.TabularInline):
    model = DetalleCompra
    form = DetalleCompraForm
    extra = 3


class DetalleCompra2InlineAdmin(admin.TabularInline):
    model = DetalleCompra2
    form = DetalleCompra2Form
    extra = 3


@register(Compra)
class Compra(admin.ModelAdmin):
    class Media:
        js = ('compra.js',)

    form = CompraForm

    change_form_template = 'compra_form.html'

    fieldsets = (
        (None, {
            'fields': [('empresa', 'sucursal')]
        }),

        (None, {
            'fields': ['numero_de_factura',]

        }),

        (None, {
            'fields': ['proveedor', 'condicion', 'fecha', 'fecha_de_vencimiento', 'orden_de_compra', 'total']
        }),
    )

    inlines = [
        DetalleCompraInlineAdmin,
        DetalleCompra2InlineAdmin,
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creado_por = request.user
        obj.save()