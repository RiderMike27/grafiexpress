from django.contrib import admin
from django.contrib.admin.decorators import register
from automoviles.models import *

# Register your models here.
@register(Automovil)
class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('marca',)
    ordering = ('marca',)
    search_fields = ('marca',)
    
