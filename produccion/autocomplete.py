from dal import autocomplete
from django.db.models import Q
from produccion.models import *
from compras.models import *
from ventas.models import *


class OrdenDeTrabajoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return OrdenDeTrabajo.objects.none()

        qs = OrdenDeTrabajo.objects.all()

        if self.q:
            qs = qs.filter(Q(id__istartswith=self.q) | Q(nombre__icontains=self.q))

        return qs.order_by('-id')


class OrdenDeTrabajoRemisionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        cliente = self.forwarded.get('cliente', None)

        if not self.request.user.is_authenticated() or not cliente:
            return OrdenDeTrabajo.objects.none()

        qs = OrdenDeTrabajo.objects.filter(cambios=False, cliente_id=cliente).exclude(restante=0).exclude(anulada=True)
        #qs = OrdenDeTrabajo.objects.filter(cambios=False, cliente_id=cliente)

        if self.q:
            qs = qs.filter(Q(id__istartswith=self.q) | Q(nombre__icontains=self.q) )

        return qs.order_by('-id')


class OrdenDeTrabajoVentaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        cliente = self.forwarded.get('cliente', None)

        if not self.request.user.is_authenticated() or not cliente:
            return OrdenDeTrabajo.objects.none()

        qs = OrdenDeTrabajo.objects.filter(cambios=False, cliente_id=cliente).exclude(cantidad_no_facturada=0).exclude(anulada=True)

        if self.q:
            qs = qs.filter(Q(id__istartswith=self.q) | Q(nombre__icontains=self.q))

        return qs.order_by('-id')


class OrdenDeTrabajoVentaChangeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        cliente = self.forwarded.get('cliente', None)

        if not self.request.user.is_authenticated() or not cliente:
            return OrdenDeTrabajo.objects.none()

        qs = OrdenDeTrabajo.objects.filter(cambios=False, cliente_id=cliente).exclude(anulada=True)

        if self.q:
            qs = qs.filter(Q(id__istartswith=self.q) | Q(nombre__icontains=self.q))

        return qs.order_by('-id')


class OrdenDeTrabajoProcesoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return OrdenDeTrabajo.objects.none()

        qs = OrdenDeTrabajo.objects.exclude(estado_produccion=EstadoProceso.FINALIZADO).exclude(anulada=True)

        if self.q:
            qs = qs.filter(Q(id__istartswith=self.q) | Q(nombre__icontains=self.q))

        return qs.order_by('-id')


class DetalleOrdenDeTrabajoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return DetalleOrdenDeTrabajo.objects.none()

        #qs = DetalleOrdenDeTrabajo.objects.exclude(pk__in=[i.detalle_orden_de_trabajo_id for i in Costo.objects.all()])
        qs = DetalleOrdenDeTrabajo.objects.all()

        if self.q:
            qs = qs.filter(Q(orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs.order_by('-id')


class DetalleOrdenDeTrabajoRemisionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        cliente = self.forwarded.get('cliente', None)

        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated() or not cliente:
            return DetalleOrdenDeTrabajo.objects.none()

        qs = DetalleOrdenDeTrabajo.objects.filter(orden_de_trabajo__cambios=True, orden_de_trabajo__cliente_id=cliente).exclude(restante=0).exclude(orden_de_trabajo__anulada=True)
        #qs = DetalleOrdenDeTrabajo.objects.filter(orden_de_trabajo__cambios=True, orden_de_trabajo__cliente_id=cliente)

        if self.q:
            qs = qs.filter(Q(orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs.order_by('-id')


class DetalleOrdenDeTrabajoVentaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        cliente = self.forwarded.get('cliente', None)

        if not self.request.user.is_authenticated() or not cliente:
            return DetalleOrdenDeTrabajo.objects.none() 

        qs = DetalleOrdenDeTrabajo.objects.filter(orden_de_trabajo__cambios=True, orden_de_trabajo__cliente_id=cliente).exclude(cantidad_no_facturada=0).exclude(orden_de_trabajo__anulada=True)

        if self.q:
            qs = qs.filter( Q(orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q) )

        return qs.order_by('-id')


class DetalleOrdenDeTrabajoVentaChangeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        cliente = self.forwarded.get('cliente', None)

        if not self.request.user.is_authenticated() or not cliente:
            return DetalleOrdenDeTrabajo.objects.none()

        #qs = DetalleOrdenDeTrabajo.objects.filter(orden_de_trabajo__cambios=True, orden_de_trabajo__cliente_id=cliente).exclude(pk__in=[i.detalle_orden_de_trabajo_id for i in DetalleDeVenta2.objects.all()])
        qs = DetalleOrdenDeTrabajo.objects.filter(orden_de_trabajo__cambios=True, orden_de_trabajo__cliente_id=cliente).exclude(orden_de_trabajo__anulada=True)

        if self.q:
            qs = qs.filter(Q(orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs.order_by('-id')


class PapelCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PapelCosto.objects.none()

        #qs = PapelCosto.objects.exclude(pk__in=[i.descripcion_id for i in PapelOrdenDeCompra.objects.all()])
        qs = PapelCosto.objects.filter(oc_incompletas=True)

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(tipo__icontains=self.q))
        return qs


class PreprensaCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PreprensaCosto.objects.none()

        qs = PreprensaCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras", "PreprensaOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(maquina__descripcion__icontains=self.q))

        return qs


class TroquelCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return TroquelCosto.objects.none()

        qs = TroquelCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras", "TroquelOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q)

        return qs


class PosprensaServicioCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PosprensaServicioCosto.objects.none()

        qs = PosprensaServicioCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","PosprensaServicioOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class PosprensaMaterialCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PosprensaMaterialCosto.objects.none()

        qs = PosprensaMaterialCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","PosprensaMaterialOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class PosprensaOtroServicioCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PosprensaOtroServicioCosto.objects.none()

        qs = PosprensaOtroServicioCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","PosprensaOtroServicioOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class DatosDeBolsaCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return DatosDeBolsaCosto.objects.none()

        qs = DatosDeBolsaCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","DatosDeBolsaOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class RevistaCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return RevistaCosto.objects.none()

        qs = RevistaCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","RevistaOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class CompuestoCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return CompuestoCosto.objects.none()

        qs = CompuestoCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","CompuestoOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class PlastificadoCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return PlastificadoCosto.objects.none()

        qs = PlastificadoCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","PlastificadoOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class OtroGastoCostoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return OtroGastoCosto.objects.none()

        qs = OtroGastoCosto.objects.exclude(pk__in=[i.descripcion_id for i in apps.get_model("compras","OtroGastoOrdenDeCompra").objects.all()])

        if self.q:
            qs = qs.filter(Q(costo__detalle_orden_de_trabajo__orden_de_trabajo__id__startswith=self.q) | Q(descripcion__icontains=self.q))

        return qs


class MaquinaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Maquina.objects.none()

        qs = Maquina.objects.filter(activa=True)

        if self.q:
            qs = qs.filter(Q(id__istartswith=self.q) | Q(nombre__icontains=self.q))
        return qs


class MaquinaProcesoAutocomplete(MaquinaAutocomplete):
    def get_queryset(self):
        qs = MaquinaAutocomplete.get_queryset(self)
        if self.forwarded['tipo']:
            qs = qs.filter(tipo=self.forwarded['tipo'])
        return qs


class DetalleProcesoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return DetalleProceso.objects.none()

        qs = DetalleProceso.objects.all()

        if self.q:
            qs = qs.filter(Q(proceso__orden_de_trabajo__id__istartswith=self.q) | Q(maquina__nombre__icontains=self.q))
        return qs


class DetalleProcesoProgramacionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        maquina = self.forwarded.get('maquina', None)

        if not self.request.user.is_authenticated() or not maquina:
            return DetalleProceso.objects.none()

        qs = DetalleProceso.objects.filter(maquina_id=maquina).exclude(estado=EstadoProceso.FINALIZADO)

        if self.q:
            qs = qs.filter(proceso__orden_de_trabajo__id__istartswith=self.q)
        return qs


class ProgramacionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Programacion.objects.none()

        qs = Programacion.objects.exclude(realizada=True)

        if self.q:
            qs = qs.filter(Q(id__istartswith=self.q) | Q(maquina__nombre__icontains=self.q))
        return qs


class DetalleProgramacionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return DetalleProgramacion.objects.none()

        qs = DetalleProgramacion.objects.all()

        if self.q:
            qs = qs.filter(Q(detalle_proceso__proceso__orden_de_trabajo__id__istartswith=self.q) | Q(
                programacion__maquina__nombre__icontains=self.q))
        return qs


class DetalleProgramacionProduccionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        programacion = self.forwarded.get('programacion', None)

        if not self.request.user.is_authenticated() or not programacion:
            return DetalleProgramacion.objects.none()

        qs = DetalleProgramacion.objects.filter(programacion_id=programacion).exclude(programacion__realizada=True)

        if self.q:
            qs = qs.filter(detalle_proceso__proceso__orden_de_trabajo__id__istartswith=self.q)
        return qs