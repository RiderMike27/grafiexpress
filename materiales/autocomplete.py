from dal import autocomplete
from django.db.models import Q
from materiales.models import *
from ventas.models import Venta


class UnidadDeMedidaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return UnidadDeMedida.objects.none()

        qs = UnidadDeMedida.objects.all()

        if self.q:
            qs = qs.filter( Q(nombre__icontains=self.q) | Q(simbolo__istartswith=self.q) )

        return qs


class CategoriaDeMaterialAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return CategoriaDeMaterial.objects.none()

        qs = CategoriaDeMaterial.objects.all()

        if self.q:
            qs = qs.filter( Q(nombre__icontains=self.q) | Q(id__istartswith=self.q) )

        return qs
        

class MaterialAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        factura = self.forwarded.get('factura', '')

        if not self.request.user.is_authenticated():
            return Material.objects.none()

        qs = Material.objects.all()

        if self.q:
            qs = qs.filter( Q(descripcion__icontains=self.q) | Q(codigo__istartswith=self.q) )

        if factura:
            qs = qs.filter(detalleventamateriales__venta_id=factura)

        return qs

class MaterialFacturaAutocomplete(MaterialAutocomplete):
    def get_queryset(self):
        queryset = super(MaterialFacturaAutocomplete, self).get_queryset()
        queryset = queryset.filter(retiro_factura=True)
        return queryset

