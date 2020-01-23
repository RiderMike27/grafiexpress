from django.contrib import admin
from django.contrib.admin.decorators import register
from ciudades.models import *

# Register your models here.
@register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)
    
