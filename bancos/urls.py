from django.conf.urls import patterns, include, url
from bancos.autocomplete import *
from bancos.views import *
from bancos.models import *

urlpatterns = [
    url(
        'bancoautocomplete/$',
        BancoAutocomplete.as_view(),
        name='banco-autocomplete',
    ),

    url(
        'cuentabancariaautocomplete/$',
        CuentaBancariaAutocomplete.as_view(),
        name='cuentabancaria-autocomplete',
    ),
    url(r'^banco/$', BancoListView.as_view(), name='banco_lis'),
    url(r'^cuentabancaria/$', CuentaBancariaListView.as_view(), name='numerocuenta_lis'),
    url(r'^$', bancos_presentacion),

]

