from django.contrib import admin
from proveedores.models import Proveedor


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('razon_social',)
    ordering = ('razon_social',)
    search_fields = ('razon_social',)


admin.site.register(Proveedor, ProveedorAdmin)