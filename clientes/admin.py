from django.contrib import admin
from django.contrib.admin.decorators import register
from clientes.models import Cliente, Marca, Contacto
from clientes.forms import *

class MarcaInlineAdmin(admin.TabularInline):
    model = Marca
    extra = 1

class ContactoInlineAdmin(admin.TabularInline):
    model = Contacto
    extra = 1

@register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'razon_social', 'ruc')
    ordering = ('nombre',)
    search_fields = ('nombre', 'razon_social', 'ruc')
    form = ClienteForm
    change_form_template = 'cliente_form.html'

    inlines = [
               MarcaInlineAdmin,
               ContactoInlineAdmin,
               ]
