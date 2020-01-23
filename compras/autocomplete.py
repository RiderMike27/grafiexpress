from dal import autocomplete
from django.db.models import Q
from compras.models import *


class FacturaPagoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        proveedor = self.forwarded.get('proveedor', None)

        # No olvides que los resultados dependen de quien los requiera!!
        if not self.request.user.is_authenticated() or not proveedor:
            return Compra.objects.none()

        qs = Compra.objects.filter(proveedor_id=proveedor).exclude(saldo=0)

        if self.q:
            qs = qs.filter(numero_de_factura__istartswith=self.q)

        return qs.order_by("-id")


class OrdenDeOrdenDeCompraAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        proveedor = self.forwarded.get('proveedor', None)

        # No olvides que los resultados dependen de quien los requiera!!
        if not self.request.user.is_authenticated() or not proveedor:
            return OrdenDeCompra.objects.none()

        qs = OrdenDeCompra.objects.filter(proveedor_id=proveedor)

        if self.q:
            qs = qs.filter(id__istartswith=self.q)

        return qs.order_by("-id")