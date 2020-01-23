from django.conf.urls import patterns, include, url

from cheques.ajax import get_monto_cheque_recibido
from cheques.autocomplete import *
from cheques.views import *

urlpatterns = [
    url(
        'chequerecibidoautocomplete/$',
        ChequeRecibidoAutocomplete.as_view(),
        name='chequerecibido-autocomplete',
    ),

    url(
        'chequeemitidoautocomplete/$',
        ChequeEmitidoAutocomplete.as_view(),
        name='chequeemitido-autocomplete',
    ),

    url(r'^chequerecibido/(?P<pk>\d+)/detail/$', ChequeRecibidoDetailView.as_view(), name='chequerecibido_det'),
    url(r'^chequerecibido/$', ChequeRecibidoListView.as_view(), name='chequerecibido_lis'),

    url(r'^chequeemitido/(?P<pk>\d+)/detail/$', ChequeEmitidoDetailView.as_view(), name='chequeemitido_det'),
    url(r'^chequeemitido/$', ChequeEmitidoListView.as_view(), name='chequeemitido_lis'),

    url('get_monto_cheque_recibido/$', get_monto_cheque_recibido),
]
