from dal import autocomplete

from comercial.models import Canal, Presupuesto


class CanalAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Canal.objects.none()
        qs = Canal.objects.filter(activo=True)
        if self.q:
            qs = qs.filter(nombre__icontains=self.q)
        return qs


class PresupuestoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Presupuesto.objects.none()
        qs = Presupuesto.objects.all()
        if self.q:
            qs = qs.filter(trabajo__icontains=self.q)

        for presupuesto in qs:
            presupuesto.trabajo = presupuesto.trabajo + " | " + presupuesto.cliente.nombre

        return qs


class PresupuestoClienteAutocomplete(PresupuestoAutocomplete):
    def get_queryset(self):
        qs = PresupuestoAutocomplete.get_queryset(self)
        if self.forwarded['cliente']:
            qs = qs.filter(cliente_id=int(self.forwarded['cliente']))
        return qs
