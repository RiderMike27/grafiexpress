from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q
from cheques.models import *
from funcionarios.models import *
from extra.globals import *


class ChequeRecibidoListView(ListView):
    model = ChequeRecibido
    template_name = "chequerecibido_list.html"
    paginate_by = 30

    def get_queryset(self):
        cheques = ChequeRecibido.objects.all()
        q = self.request.GET.get('q', '')
        if q != '':
            cheques = cheques.filter(numero__icontains=q)

        banco_id = self.request.GET.get('banco_id', '')
        if banco_id != '':
            cheques = cheques.filter(banco_id=banco_id)

        fecha_de_emision_desde = self.request.GET.get('fecha_de_emision_desde', '')
        if fecha_de_emision_desde != '':
            vector = fecha_de_emision_desde.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_emision__gte=fecha)

        fecha_de_emision_hasta = self.request.GET.get('fecha_de_emision_hasta', '')
        if fecha_de_emision_hasta != '':
            vector = fecha_de_emision_hasta.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_emision__lte=fecha)

        fecha_de_cobro_desde = self.request.GET.get('fecha_de_cobro_desde', '')
        if fecha_de_cobro_desde != '':
            vector = fecha_de_cobro_desde.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_cobro__gte=fecha)

        fecha_de_cobro_hasta = self.request.GET.get('fecha_de_cobro_hasta', '')
        if fecha_de_cobro_hasta != '':
            vector = fecha_de_cobro_hasta.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_cobro__lte=fecha)

        return cheques.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ChequeRecibidoListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['bancos'] = Banco.objects.all()
        context['banco_id'] = int(self.request.GET.get('banco_id', '')) if (self.request.GET.get('banco_id', '') != '') else ''
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''):

            lista_datos = []
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.numero,
                    dato.banco.nombre if dato.banco != None else '',
                    dato.monto,
                    dato.es_diferido,
                    dato.fecha_de_emision,
                    dato.fecha_de_cobro,
                ])

            titulos = [ 'Numero', 'Banco', 'Monto', 'Diferido', 'Fecha de Emision', 'Fecha de Cobro' ]
            return listview_to_excel(lista_datos, 'Cheques', titulos)

        return super(ChequeRecibidoListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ChequeRecibidoListView, self).dispatch(*args, **kwargs)


class ChequeRecibidoDetailView(DetailView):
    model = ChequeRecibido
    template_name = "chequerecibido_detail.html"


class ChequeEmitidoListView(ListView):
    model = ChequeEmitido
    template_name = "chequeemitido_list.html"
    paginate_by = 30

    def get_queryset(self):
        cheques = ChequeEmitido.objects.all()
        q = self.request.GET.get('q', '')
        if q != '':
            cheques = cheques.filter(numero__icontains=q)

        banco_id = self.request.GET.get('banco_id', '')
        if banco_id != '':
            cheques = cheques.filter(banco_id=banco_id)

        fecha_de_emision_desde = self.request.GET.get('fecha_de_emision_desde', '')
        if fecha_de_emision_desde != '':
            vector = fecha_de_emision_desde.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_emision__gte=fecha)

        fecha_de_emision_hasta = self.request.GET.get('fecha_de_emision_hasta', '')
        if fecha_de_emision_hasta != '':
            vector = fecha_de_emision_hasta.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_emision__lte=fecha)

        fecha_de_cobro_desde = self.request.GET.get('fecha_de_cobro_desde', '')
        if fecha_de_cobro_desde != '':
            vector = fecha_de_cobro_desde.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_cobro__gte=fecha)

        fecha_de_cobro_hasta = self.request.GET.get('fecha_de_cobro_hasta', '')
        if fecha_de_cobro_hasta != '':
            vector = fecha_de_cobro_hasta.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            cheques = cheques.filter(fecha_de_cobro__lte=fecha)

        return cheques.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ChequeEmitidoListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['bancos'] = Banco.objects.all()
        context['banco_id'] = int(self.request.GET.get('banco_id', '')) if (self.request.GET.get('banco_id', '') != '') else ''
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''):

            lista_datos = []
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.numero,
                    dato.banco.nombre if dato.banco != None else '',
                    dato.monto,
                    dato.es_diferido,
                    dato.fecha_de_emision,
                    dato.fecha_de_cobro,
                ])

            titulos = [ 'Numero', 'Banco', 'Monto', 'Diferido', 'Fecha de Emision', 'Fecha de cobro']
            return listview_to_excel(lista_datos, 'Cheques', titulos)

        return super(ChequeEmitidoListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ChequeEmitidoListView, self).dispatch(*args, **kwargs)


class ChequeEmitidoDetailView(DetailView):
    model = ChequeEmitido
    template_name = "chequeemitido_detail.html"