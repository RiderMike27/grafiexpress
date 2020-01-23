from django.conf.urls import patterns, include, url

from cobros.ajax import get_recibo
from cobros.autocomplete import CobroAutocomplete
from cobros.reports import rendicion_pdf
from cobros.views import *
from clientes.views import ClienteListView

urlpatterns = [

    url(r'^recibo/(?P<pk>\d+)/detail/$', ReciboDetailView.as_view(), name='recibo_det'),
    url(r'^recibo/$', ReciboListView.as_view(), name='recibo_lis'),
    url(r'^rendiciones/$', RendicionListView.as_view(), name='rendicion_lis'),

    url(r'^recibo/(?P<pk>\d+)/print/$', imprimir_recibo, name='recibo_print'),                       
    url(r'^recibo/(?P<pk>\d+)/cancel/$', anular_recibo, name='recibo_cancel'),
    url(r'^recibo/(?P<pk>\d+)/revert/$', cancelar_anular_recibo, name='recibo_revert'),

    url(r'^estadodecuenta/$', ClienteListView.as_view(template_name="cliente_list2.html"), name='estado_de_cuenta_lis'),
    url(r'^estadodecuenta/(?P<clienteid>\d+)/detail/$', EstadoDeCuentaListView.as_view(), name='estado_de_cuenta_det'),
    url(r'^pendientes/$', CobroListView.as_view(), name='cobros_pendientes'),
    url(
        'funcionarioautocomplete/$',
        CobroAutocomplete.as_view(),
        name='cobro-autocomplete',
    ),
    url('getrecibo/$', get_recibo),
    #REPORTES
    url(
        r'^generar_rendicion/(?P<id>\w+)/$',
        rendicion_pdf,
        name='generar_rendicion',
    ),
]

