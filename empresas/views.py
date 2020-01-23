from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

from django.contrib.auth.models import User

from empresas.models import *


class EmpresaListView(ListView):
    model = Empresa
    template_name = "empresa_list.html"

    def get_queryset(self):
        empresas = Empresa.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            empresas = empresas.filter( Q(ruc__startswith=q) | Q(nombre__icontains=q) )

        return empresas

    def get_context_data(self, **kwargs):
        context = super(EmpresaListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context
        
class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = "empresa_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EmpresaDetailView, self).get_context_data(**kwargs)
        context['sucursales'] = Sucursal.objects.filter(empresa=self.object)
        return context

class TalonarioListView(ListView):
    model = Talonario
    template_name = "talonario_list.html"

    def get_queryset(self):
        talonarios = Talonario.objects.all()

        tipo = self.request.GET.get('tipo', '')
        if tipo != '':
            talonarios = talonarios.filter(tipo_de_talonario=tipo)

        estado = self.request.GET.get('estado','')
        if estado != '':
            if estado == 'ACTIVO':
                talonarios = talonarios.filter(activo=True)
            else: #estado == 'INACTIVO'
                talonarios = talonarios.filter(activo=False)

        usuario_id = self.request.GET.get('usuario_id', '')
        if usuario_id != '':
            talonarios = talonarios.filter(usuario_id=usuario_id)

        return talonarios.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(TalonarioListView, self).get_context_data(**kwargs)
        context['tipo'] = self.request.GET.get('tipo','')
        context['estado'] = self.request.GET.get('estado','')
        context['usuarios'] = User.objects.all()
        context['usuario_id'] = int(self.request.GET.get('usuario_id','')) if (self.request.GET.get('usuario_id','') != '') else ''
        return context
        
class TalonarioDetailView(DetailView):
    model = Talonario
    template_name = "talonario_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TalonarioDetailView, self).get_context_data(**kwargs)
        return context


class TimbradoListView(ListView):
    model = Timbrado
    template_name = "timbrado_list.html"

    def get_queryset(self):
        timbrados = Timbrado.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            timbrados = timbrados.filter( numero__startswith=q )

        estado = self.request.GET.get('estado','')
        if estado != '':
            if estado == 'ACTIVO':
                timbrados = timbrados.filter(activo=True)
            else: #estado == 'INACTIVO'
                timbrados = timbrados.filter(activo=False)

        empresa_id = self.request.GET.get('empresa_id', '')
        if empresa_id != '':
            timbrados = timbrados.filter(empresa_id=empresa_id)

        return timbrados

    def get_context_data(self, **kwargs):
        context = super(TimbradoListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['estado'] = self.request.GET.get('estado','')
        context['empresas'] = Empresa.objects.all()
        context['empresa_id'] = int(self.request.GET.get('empresa_id','')) if (self.request.GET.get('empresa_id','') != '') else ''
        return context
