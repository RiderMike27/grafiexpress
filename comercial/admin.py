from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.models import User, Group

from comercial.forms import PresupuestoForm, ActividadForm
from comercial.models import Presupuesto, CantidadPresupuesto, MaterialPresupuesto, Canal, Actividad


class CantidadPresupuestoInline(admin.TabularInline):
    model = CantidadPresupuesto
    extra = 1


class MaterialPresupuestoInline(admin.TabularInline):
    model = MaterialPresupuesto
    extra = 1


@register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    inlines = (CantidadPresupuestoInline, MaterialPresupuestoInline)
    form = PresupuestoForm
    list_display = ('id',)
    ordering = ('id',)
    search_fields = ('id',)

    fieldsets = (

        (None, {
            'fields': ['cliente', 'contacto']

        }),

        (None, {
            'fields': ['trabajo', ('repeticion', 'cambios'),
                       'corte_final']
        }),

        ('Medidas', {
            'fields': [('dimensiones_x', 'dimensiones_y', 'dimensiones_z')]
        }),

        ('Color', {
            'fields': [('color_seleccion_frente', 'color_seleccion_dorso'),
                       ('color_pantone_frente', 'color_pantone_dorso')]
        }),

        (None, {
            'fields': ['terminacion',
                       ('troquelado', 'hojalado', 'despuntado'),
                       ('plastificado', 'ambas_caras'),
                       ('rel_fuego', 'numerado'),
                       'otros'
                       ]
        }),

        (None, {
            'fields': ['observaciones']

        }),

        ('Presupuesto', {
            'fields': ['adjunto']

        }),

    )


@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    actions = ['deshabilitar_canal', 'habilitar_canal']

    def get_actions(self, request):
        actions = super(CanalAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def deshabilitar_canal(self, request, queryset):
        queryset.update(activo=False)

    deshabilitar_canal.short_description = "Deshabilitar canal/es"

    def habilitar_canal(self, request, queryset):
        queryset.update(activo=True)

    habilitar_canal.short_description = "Habilitar canal/es"


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'contacto', 'vendedor')
    ordering = ('id',)
    search_fields = ('id', )
    actions = None
    form = ActividadForm


