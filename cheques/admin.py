from django.contrib import admin
from django.contrib.admin.decorators import register
from cheques.models import *
from cheques.forms import *


@register(ChequeRecibido)
class ChequeRecibidoAdmin(admin.ModelAdmin):
    form = ChequeRecibidoForm
    pass


@register(ChequeEmitido)
class ChequeEmitidoAdmin(admin.ModelAdmin):
    form = ChequeEmitidoForm
    pass
