from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.template import RequestContext
from django.shortcuts import render, render_to_response

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from extra.globals import *
from bancos.models import *


# Create your views here.
class BancoListView(ListView):
    model = Banco
    template_name = "banco_list.html"
    paginate_by = 30

    def get_queryset(self):
        bancos = Banco.objects.all()
        q = self.request.GET.get('q', '')
        if q != '':
            bancos = bancos.filter(Q(nombre__icontains=q))

        return bancos.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(BancoListView, self).get_context_data(**kwargs)
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

        return super(BancoListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(BancoListView, self).dispatch(*args, **kwargs)


class CuentaBancariaListView(ListView):
    model = CuentaBancaria
    template_name = "cuenta_bancaria_list.html"
    paginate_by = 30

    def get_queryset(self):
        cuentas_bancarias = CuentaBancaria.objects.all()
        q = self.request.GET.get('q', '')
        if q != '':
            cuentas_bancarias = cuentas_bancarias.filter(numero_de_cuenta__startswith=q)

        banco_id = self.request.GET.get('banco_id', '')
        if banco_id != '':
            cuentas_bancarias = cuentas_bancarias.filter(banco_id=banco_id)

        return cuentas_bancarias.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CuentaBancariaListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['bancos'] = Banco.objects.all()
        context['banco_id'] = int(self.request.GET.get('banco_id', '')) if (
        self.request.GET.get('banco_id', '') != '') else ''
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''):

            lista_datos = []
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.numero_de_cuenta,
                    dato.banco.nombre,
                ])

            titulos = [ 'Numero de Cuenta Bancaria', 'Banco' ]
            return listview_to_excel(lista_datos, 'CuentasBancarias', titulos)

        return super(CuentaBancariaListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(CuentaBancariaListView, self).dispatch(*args, **kwargs)


def bancos_presentacion(request):
    context = RequestContext(request)
    titulo="BANCOS"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)

