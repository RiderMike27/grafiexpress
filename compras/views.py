from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

from compras.models import *
from proveedores.models import Proveedor

from django.db.models import Sum
from extra.globals import separador_de_miles, listview_to_excel


class OrdenDeCompraDetailView(DetailView):
    model = OrdenDeCompra
    template_name = "ordendecompra_detail.html"

    def get_context_data(self, **kwargs):
        context = super(OrdenDeCompraDetailView, self).get_context_data(**kwargs)
        context['detalles0'] = PapelOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles1'] = PreprensaOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles2'] = TroquelOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles3'] = PosprensaServicioOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles4'] = PosprensaMaterialOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles5'] = PosprensaOtroServicioOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles6'] = DatosDeBolsaOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles7'] = RevistaOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles8'] = CompuestoOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles9'] = PlastificadoOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles10'] = OtroGastoOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        context['detalles11'] = InsumoOrdenDeCompra.objects.filter(orden_de_compra=self.object)
        return context


class OrdenDeCompraListView(ListView):
    model = OrdenDeCompra
    template_name = "ordendecompra_list.html"
    paginate_by = 30

    def get_queryset(self):
        ordenes_de_compras = OrdenDeCompra.objects.all()

        q=self.request.GET.get('q', '')
        if q != '':
            ordenes_de_compras = ordenes_de_compras.filter(id__istartswith=q)

        proveedor_id=self.request.GET.get('proveedor_id', '')
        if proveedor_id != '':
            ordenes_de_compras = ordenes_de_compras.filter(proveedor__id=proveedor_id)

        fecha_desde = self.request.GET.get('fecha_desde', '')
        if fecha_desde != '':
            vector = fecha_desde.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            ordenes_de_compras = ordenes_de_compras.filter(fecha__gte=fecha)

        fecha_hasta = self.request.GET.get('fecha_hasta', '')
        if fecha_hasta != '':
            vector = fecha_hasta.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            ordenes_de_compras = ordenes_de_compras.filter(fecha__lte=fecha)

        return ordenes_de_compras.order_by('-id')

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''):
            lista_datos = []
            datos = self.get_queryset()
            total_total = 0
            detalle_de_orden = ''
            for dato in datos:
                papeles = PapelOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                for papel in papeles:
                    detalle_de_orden += str(papel.descripcion)

                preprensas = PreprensaOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                for preprensa in preprensas:
                    detalle_de_orden += str(preprensa.descripcion)

                troqueles = TroquelOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                for troquel in troqueles:
                    detalle_de_orden += str(troquel.descripcion)

                posprensas_materiales = PosprensaMaterialOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                for posprensa_materiales in posprensas_materiales:
                    detalle_de_orden += str(posprensa_materiales.descripcion)

                posprensas_servicios = PosprensaServicioOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                for posprensa_servicios in posprensas_servicios:
                    detalle_de_orden += str(posprensa_servicios.descripcion)

                datos_de_bolsas = DatosDeBolsaOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                for dato_de_bolsa in datos_de_bolsas:
                    detalle_de_orden += str(dato_de_bolsa.descripcion)

                revistas = RevistaOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                compuestos = CompuestoOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                plastificados = PlastificadoOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                otros_gastos = OtroGastoOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)
                insumos = InsumoOrdenDeCompra.objects.filter(orden_de_compra_id=dato.id)

                lista_datos.append([
                    dato.fecha.strftime("%d/%m/%Y"),
                    dato.proveedor.razon_social,
                    separador_de_miles(dato.get_total()),
                    detalle_de_orden,
                ])
                total_total += dato.get_total()

            lista_datos.append(['Total', separador_de_miles(total_total)])

            titulos = ['Fecha', 'Proveedor', 'Total', 'Detalle']

            return listview_to_excel(lista_datos, 'ordenes_de_compras', titulos)

        return super(OrdenDeCompraListView, self).render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrdenDeCompraListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','')
        context['proveedores'] = Proveedor.objects.all()
        context['proveedor_id'] = int(self.request.GET.get('proveedor_id','')) if (self.request.GET.get('proveedor_id','') != '') else ''
        context['fecha_desde'] = self.request.GET.get('fecha_desde', '')
        context['fecha_hasta'] = self.request.GET.get('fecha_hasta', '')

        return context


class CompraDetailView(DetailView):
    model = Compra
    template_name = "compra_detail.html"


class CompraListView(ListView):
    model = Compra
    template_name = "compra_list.html"
    paginate_by = 30

    def get_queryset(self):
        compras = Compra.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            vector = q.split("-")
            codigo_de_establecimiento = vector[0]
            punto_de_expedicion = vector[1]
            numero_de_factura = vector[2]
            compras = compras.filter(Q(codigo_de_establecimiento__contains=codigo_de_establecimiento) &
                                    Q(punto_de_expedicion__contains=punto_de_expedicion) &
                                    Q(numero_de_factura__contains=numero_de_factura))

        proveedor_id = self.request.GET.get('proveedor_id', '')
        if proveedor_id != '':
            compras = compras.filter(proveedor__id = proveedor_id)

        fecha_de_emision_desde = self.request.GET.get('fecha_de_emision_desde', '')
        if fecha_de_emision_desde != '':
            vector = fecha_de_emision_desde.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            compras = compras.filter(fecha__gte=fecha)

        fecha_de_emision_hasta = self.request.GET.get('fecha_de_emision_hasta', '')
        if fecha_de_emision_hasta != '':
            vector = fecha_de_emision_hasta.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            compras = compras.filter(fecha__lte=fecha)

        fecha_de_vencimiento_desde = self.request.GET.get('fecha_de_vencimiento_desde', '')
        if fecha_de_vencimiento_desde != '':
            vector = fecha_de_vencimiento_desde.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            compras = compras.filter(fecha_de_vencimiento__gte=fecha)

        fecha_de_vencimiento_hasta = self.request.GET.get('fecha_de_vencimiento_hasta', '')
        if fecha_de_vencimiento_hasta != '':
            vector = fecha_de_vencimiento_hasta.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            compras = compras.filter(fecha_de_vencimiento__lte=fecha)

        return compras.order_by('-id')

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''):
            lista_datos = []
            datos = self.get_queryset()
            total_total = 0
            total_pagado = 0
            total_saldo = 0
            for dato in datos:
                lista_datos.append([
                    dato.get_numero_de_factura(),
                    dato.proveedor.razon_social,
                    dato.fecha.strftime("%d/%m/%Y"),
                    dato.fecha_de_vencimiento.strftime("%d/%m/%Y"),
                    separador_de_miles(dato.total),

                ])
                total_total += dato.total
                total_pagado += dato.pagado
                total_saldo += dato.saldo

            lista_datos.append(['', '', '', 'Total',
                                separador_de_miles(total_total)])

            titulos = ['Nro. Factura', 'Proveedor', 'Fecha Emision', 'Fecha Vencimiento', 'Total']

            return listview_to_excel(lista_datos, 'compras', titulos)

        return super(CompraListView, self).render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(CompraListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['proveedores'] = Proveedor.objects.all()
        context['proveedor_id'] = int(self.request.GET.get('proveedor_id', '')) if (self.request.GET.get('proveedor_id','') != '') else ''
        context['total_general'] = self.get_queryset().aggregate(total_general=Sum('total')).get('total_general')
        context['fecha_de_emision_desde'] = self.request.GET.get('fecha_de_emision_desde', '')
        context['fecha_de_emision_hasta'] = self.request.GET.get('fecha_de_emision_hasta', '')
        context['fecha_de_vencimiento_desde'] = self.request.GET.get('fecha_de_vencimiento_desde', '')
        context['fecha_de_vencimiento_hasta'] = self.request.GET.get('fecha_de_vencimiento_hasta', '')
        return context


def compras_presentacion(request):
    context = RequestContext(request)
    titulo = "COMPRAS"
    descripcion = "."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)


