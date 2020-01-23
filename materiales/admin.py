from django.contrib import admin
from django.contrib.admin.decorators import register
from materiales.models import *
from materiales.forms import *

@register(Resma)
class ResmaAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    list_display_links = list_display
    ordering = ('descripcion',)
    search_fields = ('descripcion',)

@register(Gramaje)
class GramajeAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    list_display_links = list_display
    ordering = ('descripcion',)
    search_fields = ('descripcion',)

@register(UnidadDeMedida)
class UnidadDeMedidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'simbolo')
    list_display_links = list_display
    ordering = ('nombre',)
    search_fields = ('nombre','simbolo')

@register(CategoriaDeMaterial)
class CategoriaDeMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = list_display
    ordering = ('id', 'nombre')
    search_fields = ('nombre','id')

@register(Material)
class MaterialAdmin(admin.ModelAdmin):
    form = MaterialForm
    change_form_template = 'material_form.html'
    
    list_display = ('codigo', 'descripcion', 'unidad_de_medida', 'categoria', 'stock_actual', 'costo_actual')
    list_display_links = list_display
    ordering = ('-stock_actual', )
    search_fields = ('codigo', 'descripcion')
    list_filter = ('categoria',)

