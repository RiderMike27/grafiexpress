from django.conf.urls import patterns, include, url
from maquinaria.autocomplete import *
from maquinaria.views import *
from maquinaria.ajax import *

urlpatterns = [
    url(
        'maquinaautocomplete/$',
        MaquinaAutocomplete.as_view(),
        name='maquina-autocomplete',
    ),

    url('getmaquina/$',get_maquina),


	#url(r'^maquina/(?P<pk>\d+)/detail/$', MaquinaDetailView.as_view(), name='maquina_det'),
	#url(r'^maquina/$', MaquinaListView.as_view(), name='maquina_lis'),

	#url(r'^$', maquina_presentacion),
]

