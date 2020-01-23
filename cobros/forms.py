from dal import autocomplete
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from clientes.models import *
from cobros.models import *
from empresas.models import *
from ventas.models import *


class ReciboForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = '__all__'
        widgets = {
            "monto": forms.TextInput(
                attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.',
                       'data-a-dec': ','}),
        }

    talonario = forms.ModelChoiceField(
        queryset=Talonario.objects.all(),
        widget=autocomplete.ModelSelect2(url='talonariorecibo-autocomplete'),
        required=True,
        label='talonario'
    )

    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=autocomplete.ModelSelect2(url='cliente-autocomplete'),
        required=True,
        label='cliente'
    )

    total_facturas = forms.CharField(widget=forms.HiddenInput(
        attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
                                     required=False)
    total_medios_de_pago = forms.CharField(widget=forms.HiddenInput(
        attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
                                           required=False)

    def __init__(self, *args, **kwargs):
        super(ReciboForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['talonario'].widget = forms.HiddenInput()
            self.initial['total_facturas'] = instance.get_total_facturas()
            self.initial['total_medios_de_pago'] = instance.get_total_medios_de_pago()

        self.fields['monto'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super(ReciboForm, self).clean()
        total_facturas = cleaned_data.get("total_facturas")
        total_medios_de_pago = cleaned_data.get("total_medios_de_pago")
        if total_facturas != total_medios_de_pago:
            msg = "Suma de montos a pagar de facturas no coinciden con suma de montos en medios de pago"
            self.add_error('monto', msg)
        pagos = DetalleDeRecibo2.objects.filter()


class DetalleDeReciboForm(forms.ModelForm):
    class Meta:
        model = DetalleDeRecibo
        fields = '__all__'
        widgets = {
            "monto": forms.TextInput(
                attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.',
                       'data-a-dec': ','}),
        }

    factura = forms.ModelChoiceField(
        queryset=Venta.objects.all(),
        widget=autocomplete.ModelSelect2(url='facturacobro-autocomplete', forward=['cliente']),
        required=False,
        label='FACTURA'
    )

    total = forms.CharField(
        widget=forms.TextInput(
            attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
        required=False,
        label="TOTAL"
    )

    pagado = forms.CharField(
        widget=forms.TextInput(
            attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
        required=False,
        label="PAGADO"
    )

    saldo = forms.CharField(
        widget=forms.TextInput(
            attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
        required=False,
        label="SALDO"
    )

    def __init__(self, *args, **kwargs):
        super(DetalleDeReciboForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['total'] = instance.factura.total
            self.initial['pagado'] = instance.factura.pagado
            self.initial['saldo'] = instance.factura.saldo
        self.fields['total'].widget.attrs['readonly'] = True
        self.fields['pagado'].widget.attrs['readonly'] = True
        self.fields['saldo'].widget.attrs['readonly'] = True


class DetalleDeRecibo2Form(forms.ModelForm):
    class Meta:
        model = DetalleDeRecibo2
        exclude = ['numero_de_comprobante', ]
        widgets = {
            "cheque": autocomplete.ModelSelect2(url='chequerecibido-autocomplete'),
            "cuenta_bancaria": autocomplete.ModelSelect2(url='cuentabancaria-autocomplete'),
            "monto": forms.TextInput(
                attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.',
                       'data-a-dec': ','}),
        }


class PresentacionCobrosForm(forms.ModelForm):
    class Meta:
        model = PresentacionCobros
        fields = '__all__'
        widgets = {
            "cobrador": autocomplete.ModelSelect2(url='funcionario-autocomplete'),
            "total": forms.TextInput(
                attrs={'style': 'text-align:right', 'readonly': 'readonly', 'size': '12', 'class': 'auto', 'data-a-sep': '.',
                       'data-a-dec': ','}),
        }


class DetallePresentacionForm(forms.ModelForm):
    class Meta:
        model = DetallePresentacion
        fields = '__all__'
        widgets = {
            "cobro": autocomplete.ModelSelect2(url='cobro-autocomplete'),
            "subtotal": forms.TextInput(
                attrs={'style': 'text-align:right', 'readonly': 'readonly', 'size': '12', 'class': 'auto', 'data-a-sep': '.',
                       'data-a-dec': ','}),
        }