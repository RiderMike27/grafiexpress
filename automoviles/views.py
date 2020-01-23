from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from extra.globals import *
from automoviles.models import *

# Create your views here.
class AutomovilListView(ListView):
    model = Automovil
    template_name = "automovil_list.html"
    paginate_by = 30

    def get_queryset(self):
        automoviles = Automovil.objects.all()
        q = self.request.GET.get('q', '')
        if q != '':
            automoviles = automoviles.filter(Q(marca__icontains=q) | Q(rua__startswith=q) | Q(rua_remolque__startswith=q))


        return automoviles.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AutomovilListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''):

            lista_datos = []
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.marca,
                    dato.rua,
                    dato.rua_remolque,

                ])

            titulos = ['Marca', 'Registro Unico del Automotor', 'Registro Unico del Automotor del Remolque o Semiremolque']
            return listview_to_excel(lista_datos, 'Automoviles', titulos)

        return super(AutomovilListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(AutomovilListView, self).dispatch(*args, **kwargs)

