from django.conf.urls import patterns, include, url
from ciudades.autocomplete import *
from ciudades.views import *

urlpatterns = [
    url(
        'ciudadautocomplete/$',
        CiudadAutocomplete.as_view(),
        name='ciudad-autocomplete',
    ),

    #url(r'^ciudad/(?P<pk>\d+)/detail/$', CiudadDetailView.as_view(), name='ciudad_det'),
    url(r'^ciudad/$', CiudadListView.as_view(), name='ciudad_lis'),
    #url(r'^$', ciudades_presentacion),
]
