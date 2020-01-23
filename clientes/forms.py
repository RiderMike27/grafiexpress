from dal import autocomplete
from django import forms

from clientes.models import *


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {"vendedor": autocomplete.ModelSelect2(url='/admin/funcionarios/funcionarioautocomplete/'),
                   "ciudad": autocomplete.ModelSelect2(url='/admin/ciudades/ciudadautocomplete/'),
                   "limite_de_credito": forms.TextInput(
                       attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.',
                              'data-a-dec': ','}),
                   "plazo_de_credito": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12'})
                   }