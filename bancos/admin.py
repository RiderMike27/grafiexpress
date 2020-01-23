from django.contrib import admin
from django.contrib.admin.decorators import register
from bancos.models import *
from bancos.forms import *


@register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)


@register(CuentaBancaria)
class CuentaBancariaAdmin(admin.ModelAdmin):
    form = CuentaBancariaForm
    pass
