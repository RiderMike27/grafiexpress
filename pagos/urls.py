from django.conf.urls import patterns, include, url
from pagos.views import *
from proveedores.views import ProveedorListView

urlpatterns = [
    url(r'^pago/(?P<pk>\d+)/detail/$', PagoDetailView.as_view(), name='pago_det'),
    url(r'^pago/$', PagoListView.as_view(), name='pago_lis'),
    url(r'^$', pagos_presentacion),

    url(r'^estadodecuenta/$', ProveedorListView.as_view(template_name="proveedor_list2.html"), name='estado_de_cuenta_lis'),
    url(r'^estadodecuenta/(?P<proveedorid>\d+)/detail/$', EstadoDeCuentaProveedorListView.as_view(), name='estado_de_cuenta_det'),
    url(r'^pendientes/$', PagosPendientesListView.as_view(), name='pagos_pendientes'),
]

