from dal import autocomplete
from django.db.models import Q

from cobros.models import Recibo


class CobroAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if not self.request.user.is_authenticated():
            return Recibo.objects.none()

        qs = Recibo.objects.exclude(estado=2).exclude(presentado=True)

        if self.q:
            qs = qs.filter(numero__icontains=self.q)

        return qs
