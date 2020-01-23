from dal import autocomplete
from django.db.models import Q
from cheques.models import *


class ChequeRecibidoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return ChequeRecibido.objects.none

        qs = ChequeRecibido.objects.all()

        if self.q:
            qs = qs.filter( Q(numero__icontains=self.q) | Q(banco__nombre__icontains=self.q) )

        return qs.order_by('-id')


class ChequeEmitidoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return ChequeEmitido.objects.none

        qs = ChequeEmitido.objects.all()

        if self.q:
            qs = qs.filter( Q(numero__icontains=self.q) | Q(banco__nombre__icontains=self.q) )

        return qs.order_by('-id')