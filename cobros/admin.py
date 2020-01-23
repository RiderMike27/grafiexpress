from django.contrib import admin
from django.contrib.admin.decorators import register
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

from cobros.models import *
from cobros.forms import *


class DetalleDeReciboInline(admin.TabularInline):
    model = DetalleDeRecibo
    form = DetalleDeReciboForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [('factura', 'total', 'pagado', 'saldo', 'monto')]
        }),
    )


class DetalleDeRecibo2Inline(admin.StackedInline):
    model = DetalleDeRecibo2
    form = DetalleDeRecibo2Form
    extra = 1


@register(Recibo)
class ReciboAdmin(admin.ModelAdmin):
    class Media:
        js = ('recibo.js',)

    form = ReciboForm

    fieldsets = (

        (None, {
            'fields': [('talonario', 'numero')]
        }),

        (None, {
            'fields': [('cliente', 'fecha')]
        }),

        (None, {
            'fields': ['monto', 'total_facturas', 'total_medios_de_pago']
        }),
    )

    inlines = [DetalleDeReciboInline, DetalleDeRecibo2Inline, ]

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.talonario.set_siguiente()
        obj.save()


class DetallePresentacionInline(admin.TabularInline):
    model = DetallePresentacion
    form = DetallePresentacionForm
    extra = 1


@register(PresentacionCobros)
class PresentacionCobrosAdmin(admin.ModelAdmin):
    class Media:
        js = ('presentacion.js',)

    list_display = ['fecha', 'cobrador', 'total']
    search_fields = ['cobrador', ]
    inlines = [DetallePresentacionInline, ]
    form = PresentacionCobrosForm

    def acciones(self,obj):
        html = '<a href="/admin/generar_rendicion/%s">Generar Reporte</a>'%obj.pk
        return mark_safe(html)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = (DetallePresentacionInline,)
        return super(PresentacionCobrosAdmin, self).change_view(request, object_id, form_url, extra_context)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/admin/cobros/rendiciones/')
