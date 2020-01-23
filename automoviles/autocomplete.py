from dal import autocomplete
from django.db.models import Q
from automoviles.models import *

class AutomovilAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Automovil.objects.none()

        qs = Automovil.objects.all()

        if self.q:
            qs = qs.filter( Q(marca__icontains=self.q) | Q(rua__istartswith=self.q) | Q(rua_remolque__istartswith=self.q) )

        return qs