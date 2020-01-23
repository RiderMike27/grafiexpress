from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from ciudades.models import Ciudad
from django.template import RequestContext
from django.shortcuts import render, render_to_response

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from extra.globals import *


class CiudadListView(ListView):
    model = Ciudad
    template_name = 'ciudad_list.html'
    paginate_by = 30



    def get_queryset(self):
        ciudades = Ciudad.objects.all()
        q = self.request.GET.get('q', '')
        if q != '':
            ciudades = ciudades.filter(Q(nombre__icontains=q))

        return ciudades.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CiudadListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''):

            lista_datos = []
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.nombre,

                ])

            titulos = ['Banco']
            return listview_to_excel(lista_datos, 'Bancos', titulos)

        return super(CiudadListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CiudadListView, self).dispatch(*args, **kwargs)