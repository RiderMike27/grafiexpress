from dal import autocomplete
from django.db.models import Q
from bancos.models import *

class BancoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Banco.objects.none

        qs = Banco.objects.all()

        if self.q:
            qs = qs.filter(nombre__icontains=self.q)

        return qs.order_by('nombre')

class CuentaBancariaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return CuentaBancaria.objects.none

        qs = CuentaBancaria.objects.all()

        if self.q:
            qs = qs.filter( Q(numero_de_cuenta__icontains=self.q) | Q(banco__nombre__icontains=self.q) )

        return qs