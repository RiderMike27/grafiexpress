from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from comercial import views
from comercial.autocomplete import PresupuestoAutocomplete, PresupuestoClienteAutocomplete
from comercial.views import PresupuestoListView, marcar_presupuesto_enviado, ActividadListView, ActividadDetailView

urlpatterns = [
    url(
            r'^presupuesto-autocomplete/$',
            PresupuestoAutocomplete.as_view(),
            name='presupuesto-autocomplete',
        ),
    url(
            r'^presupuesto-cliente-autocomplete/$',
            PresupuestoClienteAutocomplete.as_view(),
            name='presupuesto-cliente-autocomplete',
        ),
    url(
        r'^agenda/$',
        views.AgendaView.as_view(),
        name='agenda'
    ),
    url(r'^presupuesto/$',
        login_required(PresupuestoListView.as_view()),
        name='presupuesto_lis'),
    url(
        r'^presupuesto/(?P<presupuesto_id>\d+)/enviar/$',
        marcar_presupuesto_enviado,
        name='presupuesto_enviar'),

    url(
        r'^actividad/(?P<pk>\d+)/detail/$',
        ActividadDetailView.as_view(),
        name='actividad_det'),

    url(
        r'^actividad/$',
        login_required(ActividadListView.as_view()),
        name='actividad_lis'),

]
