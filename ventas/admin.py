from django.contrib import admin
from django.contrib.admin.decorators import register
from django.http import HttpResponseRedirect
from ventas.forms import *


# Register your models here.
class DetalleDeRemisionInlineAdmin(admin.TabularInline):
    model = DetalleDeRemision
    form = DetalleDeRemisionForm
    extra = 1


class DetalleDeRemision2InlineAdmin(admin.TabularInline):
    model = DetalleDeRemision2
    form = DetalleDeRemision2Form
    extra = 1


@register(Remision)
class RemisionAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    form = RemisionForm
    change_form_template = 'remision_form.html'
    inlines = [DetalleDeRemisionInlineAdmin, DetalleDeRemision2InlineAdmin ]

    fieldsets = (
        (None, {
            'fields': ['talonario', ('timbrado', 'numero_de_remision'), ('empresa', 'sucursal'), 'fecha_de_emision']
        }),

        ('DESTINATARIO DE LA MERCADERIA', {
            'fields': ['cliente']
        }),

        ('DATOS DEL TRASLADO', {
            'fields': [
                ('motivo_del_traslado', 'comprobante_de_venta'),
                ('numero_de_comprobante_de_venta', 'numero_de_timbrado'),
                'fecha_de_expedicion',
                ('fecha_de_inicio_del_traslado', 'fecha_estimada_de_termino_del_traslado'),
                'direccion_del_punto_de_partida',
                ('ciudad_de_partida', 'departamento_de_partida'),
                'direccion_del_punto_de_llegada',
                ('ciudad_de_llegada', 'departamento_de_llegada'),
                'kilometros_estimados_de_recorrido',
                'cambio_de_fecha_de_termino_del_traslado_o_punto_de_llegada',
                'motivo'
            ]
        }),

        ('DATOS DEL VEHICULO DE TRANSPORTE', {
            'fields': ['vehiculo']
        }),

        ('DATOS DEL CONDUCTOR DEL VEHICULO', {
            'fields': ['chofer']
        }),

    )

    def save_model(self, request, obj, form, change):
        if change == False:
            obj.talonario.set_siguiente()
        obj.save()

    def save_related(self, request, form, formsets, change):
        super(RemisionAdmin, self).save_related(request, form, formsets, change)
        if form.instance:
            remision = form.instance

            detalles = DetalleDeRemision.objects.filter(remision_id=remision.id)
            for detalle in detalles:
                orden_de_trabajo = detalle.orden_de_trabajo
                orden_de_trabajo.actualizar_cantidades()

            detalles = DetalleDeRemision2.objects.filter(remision_id=remision.id)
            for detalle in detalles:
                orden_de_trabajo = detalle.detalle_orden_de_trabajo.orden_de_trabajo
                orden_de_trabajo.actualizar_cantidades()


class DetalleDeVentaInlineAdmin(admin.TabularInline):
    model = DetalleDeVenta
    form = DetalleDeVentaForm
    extra = 3


class DetalleDeVentaChangeInlineAdmin(admin.TabularInline):
    model = DetalleDeVenta
    form = DetalleDeVentaChangeForm
    extra = 3


class DetalleDeVenta2InlineAdmin(admin.TabularInline):
    model = DetalleDeVenta2
    form = DetalleDeVenta2Form
    extra = 3


class DetalleDeVenta2ChangeInlineAdmin(admin.TabularInline):
    model = DetalleDeVenta2
    form = DetalleDeVenta2ChangeForm
    extra = 3


class DetalleVentaMaterialInlineAdmin(admin.TabularInline):
    model = DetalleVentaMateriales
    form = DetalleVentaMaterialForm
    extra = 3


@register(Venta)
class VentaAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    form = VentaForm
    change_form_template = 'venta_form.html'
    inlines = []

    fieldsets = (
        (None, {
            'fields': [
                'talonario', 
                ('timbrado', 'numero_de_factura'), 
                ('empresa', 'sucursal'),
                'cliente',
                'condicion',
                ('fecha_de_emision', 'fecha_de_vencimiento')
            ]
        }),

        (None, {
            'fields': [
                'remision',
                'total'
            ]
        }),
    )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = (DetalleDeVentaChangeInlineAdmin, DetalleDeVenta2ChangeInlineAdmin, DetalleVentaMaterialInlineAdmin)
        return super(VentaAdmin, self).change_view(request, object_id, form_url, extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = (DetalleDeVentaInlineAdmin, DetalleDeVenta2InlineAdmin, DetalleVentaMaterialInlineAdmin)
        return super(VentaAdmin, self).add_view(request, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.talonario.set_siguiente()
        obj.save()

    def save_related(self, request, form, formsets, change):
        super(VentaAdmin, self).save_related(request, form, formsets, change)
        if form.instance:
            venta = form.instance

            detalles = DetalleDeVenta.objects.filter(venta_id=venta.id)
            for detalle in detalles:
                orden_de_trabajo = detalle.orden_de_trabajo
                orden_de_trabajo.actualizar_cantidades_facturadas()

            detalles = DetalleDeVenta2.objects.filter(venta_id=venta.id)
            for detalle in detalles:
                orden_de_trabajo = detalle.detalle_orden_de_trabajo.orden_de_trabajo
                orden_de_trabajo.actualizar_cantidades_facturadas()

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if obj == None:
            return True

        if obj.estado == PENDIENTE:
            return True

        return False


@register(VentaAntiguo)
class VentaAntiguoAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    form = VentaAntiguoForm
    change_form_template = 'venta_form.html'
    inlines = [DetalleDeVentaInlineAdmin, DetalleDeVenta2InlineAdmin, DetalleVentaMaterialInlineAdmin]

    fieldsets = (
        (None, {
            'fields': [ 
                'talonario', 
                ('timbrado', 'numero_de_factura'), 
                ('empresa', 'sucursal'),
                'condicion',
                ('fecha_de_emision', 'fecha_de_vencimiento'),
                'cliente'
            ]
        }),

        (None, {
            'fields': [
                'remision',
                'total'
            ]
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if obj == None:
            return True

        if obj.estado == PENDIENTE:
            return True

        return False

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect('/admin/ventas/venta')

    def response_change(self, request, obj):
        return HttpResponseRedirect('/admin/ventas/venta')



@register(RemisionAntiguo)
class RemisionAntiguoAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    form = RemisionAntiguoForm
    change_form_template = 'remision_form.html'
    inlines = [DetalleDeRemisionInlineAdmin, DetalleDeRemision2InlineAdmin ]

    fieldsets = (
        (None, {
            'fields': ['talonario', ('timbrado', 'numero_de_remision'), ('empresa', 'sucursal'), 'fecha_de_emision']
        }),

        ('DESTINATARIO DE LA MERCADERIA', {
            'fields': ['cliente']
        }),

        ('DATOS DEL TRASLADO', {
            'fields': [
                ('motivo_del_traslado', 'comprobante_de_venta'),
                ('numero_de_comprobante_de_venta', 'numero_de_timbrado'),
                'fecha_de_expedicion',
                ('fecha_de_inicio_del_traslado', 'fecha_estimada_de_termino_del_traslado'),
                'direccion_del_punto_de_partida',
                ('ciudad_de_partida', 'departamento_de_partida'),
                'direccion_del_punto_de_llegada',
                ('ciudad_de_llegada', 'departamento_de_llegada'),
                'kilometros_estimados_de_recorrido',
                'cambio_de_fecha_de_termino_del_traslado_o_punto_de_llegada',
                'motivo'
            ]
        }),

        ('DATOS DEL VEHICULO DE TRANSPORTE', {
            'fields': ['vehiculo']
        }),

        ('DATOS DEL CONDUCTOR DEL VEHICULO', {
            'fields': ['chofer']
        }),

    )

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect('/admin/ventas/remision')

    def response_change(self, request, obj):
        return HttpResponseRedirect('/admin/ventas/remision')

    def save_related(self, request, form, formsets, change):
        super(RemisionAntiguoAdmin, self).save_related(request, form, formsets, change)
        if form.instance:
            remision = form.instance

            detalles = DetalleDeRemision.objects.filter(remision_id=remision.id)
            for detalle in detalles:
                orden_de_trabajo = detalle.orden_de_trabajo
                orden_de_trabajo.actualizar_cantidades()

            detalles = DetalleDeRemision2.objects.filter(remision_id=remision.id)
            for detalle in detalles:
                orden_de_trabajo = detalle.detalle_orden_de_trabajo.orden_de_trabajo
                orden_de_trabajo.actualizar_cantidades()