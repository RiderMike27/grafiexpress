from django.contrib import admin
from django.contrib.admin.decorators import register
from maquinaria.models import *
from maquinaria.forms import *

@register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    form = MaquinaForm
    change_form_template = 'maquina_form.html'
    
    list_display = ('id', 'descripcion', 'precio')
    list_display_links = ('id', 'descripcion')
    ordering = ('id', 'descripcion')
    search_fields = ('id', 'descripcion')
