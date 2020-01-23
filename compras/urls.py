from django.conf.urls import patterns, include, url
from compras.reports import *
from compras.views import *
from compras.ajax import *
from compras.autocomplete import *

urlpatterns = patterns('',

                       url(
                           'facturapagoautocomplete/$',
                           FacturaPagoAutocomplete.as_view(),
                           name='facturapago-autocomplete',
                       ),

                       url(
                           'ordendecompraautocomplete/$',
                           OrdenDeOrdenDeCompraAutocomplete.as_view(),
                           name='ordendecompra-autocomplete',
                       ),

                       url(r'^compra/$', CompraListView.as_view(), name='compra_lis'),
                       url(r'^compra/(?P<pk>\d+)/detail/$', CompraDetailView.as_view(), name='compra_det'),

                       url(r'^ordendecompra/$', OrdenDeCompraListView.as_view(), name='ordendecompra_lis'),
                       url(r'^ordendecompra/(?P<pk>\d+)/detail/$', OrdenDeCompraDetailView.as_view(),
                           name='ordendecompra_det'),
                       url(r'^ordendecompra/(?P<orden_de_compra_id>\d+)/print/$', reporte_orden_de_compra,
                           name='reporte_orden_de_compra'),

                       url('getcompra/$', get_compra),
                       url('get_plazo_credito/$', get_plazo_credito),
                       url(r'^$', compras_presentacion),
                       )
