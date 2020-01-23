from django.contrib import admin
from django.contrib.admin.decorators import register

from pagos.models import *
from pagos.forms import *

class DetalleDePagoInline(admin.TabularInline):
    model = DetalleDePago
    form = DetalleDePagoForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [('compra', 'total', 'pagado','saldo', 'monto')]
        }),
    )


class DetalleDePago2Inline(admin.StackedInline):
    model = DetalleDePago2
    form = DetalleDePago2Form
    extra = 1

    fieldsets = (

        (None, {
            'fields': [('medio_de_pago', 'numero_de_comprobante')]
        }),

        (None, {
            'fields': ['cheque']
        }),

        (None, {
            'fields': ['cuenta_bancaria']
        }),

        (None, {
            'fields': ['monto']
        }),
    )



@register(Pago)
class PagoAdmin(admin.ModelAdmin):
    class Media:
        js = ('pago.js',)

    form = PagoForm

    fieldsets = (

        (None, {
            'fields': [('proveedor', 'fecha')]
        }),

        (None, {
            'fields': ['monto', 'total_facturas', 'total_medios_de_pago']
        }),
    )

    inlines = [DetalleDePagoInline, DetalleDePago2Inline,]



