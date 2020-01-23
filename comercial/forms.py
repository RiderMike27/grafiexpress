from dal import autocomplete
from django import forms

from comercial.models import Presupuesto, Actividad, Canal


class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'
        widgets = {
            "cliente": autocomplete.ModelSelect2(url='/admin/clientes/cliente/clienteautocomplete/'),
            "contacto": autocomplete.ModelSelect2(url='contacto-cliente-autocomplete',  forward=['cliente']),
        }


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
        widgets = {
            "cliente": autocomplete.ModelSelect2(url='/admin/clientes/cliente/clienteautocomplete/'),
            "contacto": autocomplete.ModelSelect2(url='contacto-cliente-autocomplete', forward=['cliente']),
            'marca': autocomplete.ModelSelect2(url='marca-cliente-autocomplete', forward=['cliente']),
            'presupuesto': autocomplete.ModelSelect2(url='presupuesto-cliente-autocomplete'),
            'actividad_id': forms.HiddenInput(attrs={
                'type': 'hidden'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['readonly'] = True


