from dal import autocomplete
from django.db.models import Q
from clientes.models import *


class ClienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Cliente.objects.none()
        qs = Cliente.objects.exclude(activo=False)
        if self.q:
            qs = qs.filter( Q(nombre__icontains=self.q) | Q(razon_social__icontains=self.q) | Q(razon_social__istartswith=self.q) | Q(ruc__istartswith=self.q) )
        return qs


class MarcaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Marca.objects.none()
        qs = Marca.objects.all()
        if self.q:
            qs = qs.filter( nombre__icontains=self.q )
        return qs


class MarcaClienteAutocomplete(MarcaAutocomplete):
    def get_queryset(self):
        qs = MarcaAutocomplete.get_queryset(self)
        if self.forwarded['cliente']:
            qs = qs.filter(cliente_id=int(self.forwarded['cliente']))
        return qs


class ContactoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Contacto.objects.none()
        qs = Contacto.objects.all()
        if self.q:
            qs = qs.filter(nombre__icontains=self.q)
        return qs


class ContactoClienteAutocomplete(ContactoAutocomplete):
    def get_queryset(self):
        qs = ContactoAutocomplete.get_queryset(self)
        if self.forwarded['cliente']:
            qs = qs.filter(cliente_id=int(self.forwarded['cliente']))
        return qs
