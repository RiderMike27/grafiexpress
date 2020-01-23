from django.conf.urls import patterns, include, url
from automoviles.autocomplete import *
from automoviles.views import *

urlpatterns = [
    url(
        'automovilautocomplete/$',
        AutomovilAutocomplete.as_view(),
        name='automovil-autocomplete',
    ),

    #url(r'^automovil/(?P<pk>\d+)/detail/$', AutomovilDetailView.as_view(), name='automovil_det'),
    url(r'^automovil/$', AutomovilListView.as_view(), name='automovil_lis'),
    #url(r'^$', automoviles_presentacion),
]
