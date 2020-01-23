from django.conf.urls import patterns, include, url
from produccion.autocomplete import *
from produccion.views import *
from produccion.ajax import *
from produccion.reports import *


urlpatterns = patterns('',

    url(
        r'^ordendetrabajoautocomplete/$',
        OrdenDeTrabajoAutocomplete.as_view(),
        name='ordendetrabajo-autocomplete',
    ),

    url(
        r'^ordendetrabajoremisionautocomplete/$',
        OrdenDeTrabajoRemisionAutocomplete.as_view(),
        name='ordendetrabajoremision-autocomplete',
    ),

    url(
        r'^ordendetrabajoventaautocomplete/$',
        OrdenDeTrabajoVentaAutocomplete.as_view(),
        name='ordendetrabajoventa-autocomplete',
    ),

    url(
        r'^ordendetrabajoventachangeautocomplete/$',
        OrdenDeTrabajoVentaChangeAutocomplete.as_view(),
        name='ordendetrabajoventachange-autocomplete',
    ),

    url(
        r'^ordendetrabajoprocesoautocomplete/$',
        OrdenDeTrabajoProcesoAutocomplete.as_view(),
        name='ordendetrabajoproceso-autocomplete',
    ),

    url(
        r'^detalleordendetrabajoautocomplete/$',
        DetalleOrdenDeTrabajoAutocomplete.as_view(),
        name='detalleordendetrabajo-autocomplete',
    ),

    url(
        r'^detalleordendetrabajoventaautocomplete/$',
        DetalleOrdenDeTrabajoVentaAutocomplete.as_view(),
        name='detalleordendetrabajoventa-autocomplete',
    ),

    url(
       r'^detalleordendetrabajoventachangeautocomplete/$',
       DetalleOrdenDeTrabajoVentaChangeAutocomplete.as_view(),
       name='detalleordendetrabajoventachange-autocomplete',
    ),

    url(
        r'^detalleordendetrabajoremisionautocomplete/$',
        DetalleOrdenDeTrabajoRemisionAutocomplete.as_view(),
        name='detalleordendetrabajoremision-autocomplete',
    ),

    url(
        r'^papelcostoautocomplete/$',
        PapelCostoAutocomplete.as_view(),
        name='papelcosto-autocomplete',
    ),

    url(
        r'^preprensacostoautocomplete/$',
        PreprensaCostoAutocomplete.as_view(),
        name='preprensacosto-autocomplete',
    ),

    url(
        r'^troquelcostoautocomplete/$',
        TroquelCostoAutocomplete.as_view(),
        name='troquelcosto-autocomplete',
    ),

    url(
        r'^posprensaserviciocostoautocomplete/$',
        PosprensaServicioCostoAutocomplete.as_view(),
        name='posprensaserviciocosto-autocomplete',
    ),

    url(
        r'^posprensamaterialcostoautocomplete/$',
        PosprensaMaterialCostoAutocomplete.as_view(),
        name='posprensamaterialcosto-autocomplete',
    ),

    url(
        r'^posprensaotroserviciocostoautocomplete/$',
        PosprensaOtroServicioCostoAutocomplete.as_view(),
        name='posprensaotroserviciocosto-autocomplete',
    ),

    url(
        r'^datosdebolsacostoautocomplete/$',
        DatosDeBolsaCostoAutocomplete.as_view(),
        name='datosdebolsacosto-autocomplete',
    ),

    url(
        r'^revistacostoautocomplete/$',
        RevistaCostoAutocomplete.as_view(),
        name='revistacosto-autocomplete',
    ),

    url(
        r'^compuestocostoautocomplete/$',
        CompuestoCostoAutocomplete.as_view(),
        name='compuestocosto-autocomplete',
    ),

    url(
        r'^plastificadocostoautocomplete/$',
        PlastificadoCostoAutocomplete.as_view(),
        name='plastificadocosto-autocomplete',
    ),

    url(
        r'^otrogastocostoautocomplete/$',
        OtroGastoCostoAutocomplete.as_view(),
        name='otrogastocosto-autocomplete',
    ),

    url(
        r'^maquinaautocomplete/$',
        MaquinaAutocomplete.as_view(),
        name='maquina-autocomplete',
    ),

    url(
        r'^maquinaprocesoautocomplete/$',
        MaquinaProcesoAutocomplete.as_view(),
        name='maquina-proceso-autocomplete',
    ),

    url(
        r'^detalleprocesoautocomplete/$',
        DetalleProcesoAutocomplete.as_view(),
        name='detalleproceso-autocomplete',
    ),
    url(
        r'^detalleprocesoprogramacionautocomplete/$',
        DetalleProcesoProgramacionAutocomplete.as_view(),
        name='detalleproceso-programacion-autocomplete',
    ),
    url(
        r'^programacionautocomplete/$',
        ProgramacionAutocomplete.as_view(),
        name='programacion-autocomplete',
    ),
    url(
        r'^detalleprogramacionautocomplete/$',
        DetalleProgramacionAutocomplete.as_view(),
        name='detalleprogramacion-autocomplete',
    ),
    url(
        r'^detalleprogramacionproduccionautocomplete/$',
        DetalleProgramacionProduccionAutocomplete.as_view(),
        name='detalleprogramacion-produccion-autocomplete',
    ),

    url(r'^getordendetrabajo/$',get_ordendetrabajo),

    url(r'^getdetalleordendetrabajo/$',get_detalleordendetrabajo),

    url(r'^getpapelcosto/$',get_papelcosto),

    url(r'^getpreprensacosto/$',get_preprensacosto),

    url(r'^gettroquelcosto/$',get_troquelcosto),

    url(r'^getposprensaserviciocosto/$',get_posprensaserviciocosto),

    url(r'^getposprensamaterialcosto/$',get_posprensamaterialcosto),

    url(r'^getposprensaotroserviciocosto/$',get_posprensaotroserviciocosto),

    url(r'^getdatosdebolsacosto/$',get_datosdebolsacosto),

    url(r'^getrevistacosto/$',get_revistacosto),

    url(r'^getcompuestocosto/$',get_compuestocosto),

    url(r'^getplastificadocosto/$',get_plastificadocosto),

    url(r'^getotrogastocosto/$',get_otrogastocosto),

    url(r'^getmaquina/$', get_maquina),

    url(r'^getdetalleproceso/$', get_detalle_proceso),
    url(r'^getdetalleprogramacion/$', get_detalle_programacion),

    url(r'^categoriadetrabajo/$', CategoriaDeTrabajoListView.as_view(), name='categoriadetrabajo_lis'),
    url(r'^categoriadetrabajo/(?P<pk>\d+)/detail/$', CategoriaDeTrabajoDetailView.as_view(), name='categoriadetrabajo_det'),
    
    url(r'^costo/$', CostoListView.as_view(), name='costo_lis'),
    url(r'^costo/(?P<pk>\d+)/detail/$', CostoDetailView.as_view(), name='costo_det'),

    url(r'^programacion/$', ProgramacionListView.as_view(), name='programacion_lis'),
    url(r'^proceso/$', ProcesoListView.as_view(), name='proceso_lis'),
    url(r'^produccion/$', ProduccionListView.as_view(), name='produccion_lis'),
    
    url(r'^ordendetrabajo/$', login_required(OrdenDeTrabajoListView.as_view()), name='ordendetrabajo_lis'),
    url(r'^ordendetrabajo/(?P<pk>\d+)/detail/$', OrdenDeTrabajoDetailView.as_view(), name='ordendetrabajo_det'),
    
    url(r'^ordendetrabajo/(?P<orden_de_trabajo_id>\d+)/print/$', reporte_orden_de_trabajo, name='ordendetrabajo_print'),
    url(
        r'^calendario_por_maquina/(?P<id>\w+)/$',
        calendario_por_maquina,
        name='calendario_por_maquina',
    ),
    url(
        r'^maquina/(?P<pk>\d+)/agenda/$',
        AgendaMaquinaDetailView.as_view(),
        name='agendamaquina_det'
      ),

    url(r'^ordendetrabajo/(?P<orden_de_trabajo_id>\d+)/aprobar/$', marcar_orden_de_trabajo_aprobada, name='ordendetrabajo_aprobar'),
    url(r'^ordendetrabajo/(?P<orden_de_trabajo_id>\d+)/desaprobar/$', marcar_orden_de_trabajo_desaprobada, name='ordendetrabajo_desaprobar'),
    url(r'^ordendetrabajo/(?P<orden_de_trabajo_id>\d+)/delete/$', anular_orden_de_trabajo, name='ordendetrabajo_anular'),
    url(r'^ordendetrabajo/(?P<orden_de_trabajo_id>\d+)/undelete/$', desanular_orden_de_trabajo, name='ordendetrabajo_desanular'),



    url(r'^$', produccion_presentacion),
)
