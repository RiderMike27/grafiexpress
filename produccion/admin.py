from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.models import _user_has_perm
from django.utils.safestring import mark_safe

from produccion.forms import *


class ArchivoOrdenDeTrabajoInline(admin.TabularInline):
    model = ArchivoOrdenDeTrabajo
    extra = 1


class DetalleOrdenDeTrabajoInline(admin.StackedInline):
    model = DetalleOrdenDeTrabajo
    form = DetalleOrdenDeTrabajoForm
    extra = 1

    fieldsets = (

        (None, {
            'fields': [('descripcion', 'cantidad')]
        }),

        (None, {
            'description': 'Dimensiones',
            'fields': [('dimensiones_x', 'dimensiones_y', 'dimensiones_z')]
        }),

        (None, {
            'fields': [('material', 'marca'), ('gramaje', 'resma')]
        }),

        (None, {
            'description': 'Seleccion',
            'fields': [('color_seleccion_frente', 'color_seleccion_dorso')]
        }),

        (None, {
            'description': 'Pantone',
            'fields': [('color_pantone_frente', 'color_pantone_dorso')]
        }),

        (None, {
            'fields': ['observaciones']
        }),
    )


@register(OrdenDeTrabajo)
class OrdenDeTrabajoAdmin(admin.ModelAdmin):
    inlines = (DetalleOrdenDeTrabajoInline, ArchivoOrdenDeTrabajoInline)
    form = OrdenDeTrabajoForm
    list_display = ('id',)
    ordering = ('id',)
    search_fields = ('id',)

    change_form_template = 'ordendetrabajo_form.html'
    datos_trabajo = ('presupuesto_numero', 'presupuesto_item', 'fecha_de_ingreso', 'fecha_solicitada', 'comentarios')
    default_fieldsets = (
            ('General', {
                'fields': (
                    ('numero','automatico'),
                    'nombre', 
                    ('cliente', 'limite_de_credito', 'marca', 'contacto'),
                    ('vendedor', 'orden_de_compra_del_cliente')
                )
            }),

        ('Datos del Trabajo', {
            'fields': datos_trabajo
        }),

        ('Opciones', {
            'fields': ('prueba_de_color', 'muestra_de_color', 'prueba_de_producto', 'muestra_de_producto', 'originales',
                       'repeticion', 'buscar_sobrante')
        }),

        ('Detalle', {
            'fields': (('categoria', 'subcategoria'),
                       ('cantidad', 'cambios', 'materiales_compuestos', 'precio_unitario', 'total', 'suma_cantidad'),)
        }),
    )

    fieldsets = default_fieldsets

    def view_fecha_solicitada(self, request):
        if not request.user.has_perm('produccion.view_fecha_solicitada'):
            self.fieldsets[1][1]['fields'] = [s for s in self.datos_trabajo if s != 'fecha_solicitada']
        else:
            self.fieldsets[1][1]['fields'] = self.datos_trabajo

    def add_view(self, request, form_url='', extra_context=None):
        self.view_fecha_solicitada(request)
        return super(OrdenDeTrabajoAdmin, self).add_view(request,
                                                         form_url=form_url,
                                                         extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.view_fecha_solicitada(request)
        return super(OrdenDeTrabajoAdmin, self).change_view(request, object_id,
                                                            form_url=form_url,
                                                            extra_context=extra_context)

    def save_related(self, request, form, formsets, change):
        super(OrdenDeTrabajoAdmin, self).save_related(request, form, formsets, change)
        if form.instance:
            obj = form.instance
            obj.actualizar_cantidades()
            obj.actualizar_cantidades_facturadas()

    def get_form(self, request, obj=None, **kwargs):
        form = super(OrdenDeTrabajoAdmin, self).get_form(request, obj=None, **kwargs)
        form.current_user = request.user
        return form


class SubcategoriaDeTrabajoInline(admin.TabularInline):
    model = SubcategoriaDeTrabajo
    extra = 1


@register(CategoriaDeTrabajo)
class CategoriaDeTrabajoAdmin(admin.ModelAdmin):
    inlines = (SubcategoriaDeTrabajoInline,)
    list_display = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)


class PapelCostoInline(admin.TabularInline):
    model = PapelCosto
    form = PapelCostoForm
    extra = 1
    template = 'costo_tabular.html'


class PreprensaCostoInline(admin.TabularInline):
    model = PreprensaCosto
    form = PreprensaCostoForm
    extra = 1
    template = 'costo_tabular.html'


class TroquelCostoInline(admin.TabularInline):
    model = TroquelCosto
    form = TroquelCostoForm
    extra = 1
    template = 'costo_tabular.html'


class PosprensaServicioCostoInline(admin.TabularInline):
    model = PosprensaServicioCosto
    form = PosprensaServicioCostoForm
    extra = 1
    template = 'costo_tabular.html'


class PosprensaMaterialCostoInline(admin.TabularInline):
    model = PosprensaMaterialCosto
    form = PosprensaMaterialCostoForm
    extra = 1
    template = 'costo_tabular.html'


class PosprensaOtroServicioCostoInline(admin.TabularInline):
    model = PosprensaOtroServicioCosto
    form = PosprensaOtroServicioCostoForm
    extra = 1
    template = 'costo_tabular.html'


class DatosDeBolsaCostoInline(admin.TabularInline):
    model = DatosDeBolsaCosto
    form = DatosDeBolsaCostoForm
    extra = 1
    template = 'costo_tabular.html'


class RevistaCostoInline(admin.TabularInline):
    model = RevistaCosto
    form = RevistaCostoForm
    extra = 1
    template = 'costo_tabular.html'


class CompuestoCostoInline(admin.TabularInline):
    model = CompuestoCosto
    form = CompuestoCostoForm
    extra = 1
    template = 'costo_tabular.html'


class PlastificadoCostoInline(admin.TabularInline):
    model = PlastificadoCosto
    form = PlastificadoCostoForm
    extra = 1
    template = 'costo_tabular.html'


class OtroGastoCostoInline(admin.TabularInline):
    model = OtroGastoCosto
    form = OtroGastoCostoForm
    extra = 1
    template = 'costo_tabular.html'


@register(Costo)
class CostoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    form = CostoForm

    change_form_template = 'costo_form.html'

    fieldsets = (
        (None, {
            'fields': [('detalle_orden_de_trabajo', 'vendedor')]
        }),

        (None, {
            'fields': [('orden_de_trabajo', 'cantidad', 'presupuesto'), ('cliente', 'fecha')]
        }),

        (None, {
            'fields': (
                'total_papel', 'total_preprensa', 'total_troquel',
                'total_posprensaservicio', 'total_posprensamaterial', 'total_posprensaotroservicio',
                'total_datosdebolsa', 'total_revista', 'total_compuesto', 'total_plastificado',
                'total_general', 'total_iva'
            )
        }),
    )

    inlines = [
        PapelCostoInline,
        PreprensaCostoInline,
        TroquelCostoInline,
        PosprensaServicioCostoInline,
        PosprensaMaterialCostoInline,
        PosprensaOtroServicioCostoInline,
        DatosDeBolsaCostoInline,
        RevistaCostoInline,
        CompuestoCostoInline,
        PlastificadoCostoInline,
        OtroGastoCostoInline,
    ]


@register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pasadas_por_hora', 'tipo', 'fecha_disponible', 'hora_disponible', 'acciones')
    search_fields = ('nombre',)
    list_filter = ('tipo', )
    actions = None

    def acciones(self, obj):
        html = '<a href="/admin/produccion/maquina/%s/agenda">Ver Agenda</a>'%obj.pk
        return mark_safe(html)


class DetalleProcesoAdmin(admin.TabularInline):
    model = DetalleProceso
    form = DetalleProcesoForm

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


@register(Proceso)
class ProcesoAdmin(admin.ModelAdmin):
    class Media:
        js = ('proceso.js',)
    form = ProcesoForm
    inlines = (DetalleProcesoAdmin, )
    list_display = ('fecha_de_creacion', 'orden_de_trabajo', 'estado_ot', 'get_procesos_realizados')
    search_fields = ('orden_de_trabajo__id', )
    actions = None


class DetalleProgramacionInline(admin.TabularInline):
    model = DetalleProgramacion
    form = DetalleProgramacionForm

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


@register(Programacion)
class ProgramacionAdmin(admin.ModelAdmin):
    class Media:
        js = ('programacion.js',)
    inlines = (DetalleProgramacionInline, )
    list_filter = ('maquina',)
    actions = None
    list_display = ('id', 'maquina', 'fecha_de_inicio', 'reporte', 'realizada')
    form = ProgramacionForm

    def reporte(self, obj):
        html = '<a href="/admin/produccion/calendario_por_maquina/%s">Calendario</a>'%obj.pk
        return mark_safe(html)


class DetalleProduccionInline(admin.TabularInline):
    model = DetalleProduccion
    form = DetalleProduccionForm

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1


@register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    class Media:
        js = ('produccion.js',)

    inlines = (DetalleProduccionInline, )
    list_display = ('id', 'programacion', 'fecha_de_creacion')
    actions = None
    form = ProduccionForm
