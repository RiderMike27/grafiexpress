from dal import autocomplete
from django.db.models import Q
from maquinaria.models import *

class MaquinaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Maquina.objects.none()

        qs = Maquina.objects.all()

        if self.q:
            qs = qs.filter( Q(descripcion__icontains=self.q) | Q(id__istartswith=self.q) )

        return qs