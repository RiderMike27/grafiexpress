from django.conf.urls import patterns, include, url
from clientes.autocomplete import *
from clientes.views import *
from clientes.ajax import get_cliente, get_clientedecontacto

urlpatterns = [
    url(
        'clienteautocomplete/$',
        ClienteAutocomplete.as_view(),
        name='cliente-autocomplete',
    ),

    url(
        'marcaautocomplete/$',
        MarcaAutocomplete.as_view(),
        name='marca-autocomplete',
    ),

    url(
        'marca-cliente-autocomplete/$',
        MarcaClienteAutocomplete.as_view(),
        name='marca-cliente-autocomplete',
    ),

    url(
        'contactoautocomplete/$',
        ContactoAutocomplete.as_view(),
        name='contacto-autocomplete',
    ),

    url(
        'contacto-cliente-autocomplete/$',
        ContactoClienteAutocomplete.as_view(),
        name='contacto-cliente-autocomplete',
    ),

    url('getcliente/$', get_cliente),

    url('get_clientedecontacto/$', get_clientedecontacto),

    url(r'^cliente/(?P<pk>\d+)/detail/$', ClienteDetailView.as_view(), name='cliente_det'),
    url(r'^cliente/$', ClienteListView.as_view(), name='cliente_lis'),
    url(r'^$', clientes_presentacion),
]

