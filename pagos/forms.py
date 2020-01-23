from dal import autocomplete
from django import forms

from pagos.models import *
from compras.models import *
from proveedores.models import *

class PagoForm(forms.ModelForm):
	class Meta:
		model = Pago
		fields = ('__all__')
		widgets = { 
			"monto":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}


	proveedor = forms.ModelChoiceField(
		queryset=Proveedor.objects.all(),
		widget= autocomplete.ModelSelect2(url='proveedor-autocomplete'),
		required=True,
		label='proveedor'
	)

	total_facturas = forms.CharField(widget=forms.HiddenInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),required=False)
	total_medios_de_pago = forms.CharField(widget=forms.HiddenInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),required=False)

	def __init__(self, *args, **kwargs):
		super(PagoForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.initial['total_facturas'] = instance.get_total_facturas()
			self.initial['total_medios_de_pago'] = instance.get_total_medios_de_pago()

		self.fields['monto'].widget.attrs['readonly'] = True

	def clean(self):
		cleaned_data = super(PagoForm, self).clean()
		total_facturas = cleaned_data.get("total_facturas")
		total_medios_de_pago = cleaned_data.get("total_medios_de_pago")
		if (total_facturas != total_medios_de_pago):
			msg = "Suma de montos a pagar de facturas no coinciden con suma de montos en medios de pago"
			self.add_error('monto', msg)


class DetalleDePagoForm(forms.ModelForm):
	class Meta:
		model = DetalleDePago
		fields = ('__all__')
		widgets = { 
			"monto":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}

	compra = forms.ModelChoiceField(
		queryset=Compra.objects.all(),
		widget= autocomplete.ModelSelect2(url='facturapago-autocomplete', forward=['proveedor']),
		required=True,
		label='FACTURA'
	)

	total = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="TOTAL"
	)

	pagado = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="PAGADO"
	)

	saldo = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="SALDO"
	)

	def __init__(self, *args, **kwargs):
		super(DetalleDePagoForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.initial['total'] = instance.compra.total
			self.initial['pagado'] = instance.compra.pagado
			self.initial['saldo'] = instance.compra.saldo
		self.fields['total'].widget.attrs['readonly'] = True
		self.fields['pagado'].widget.attrs['readonly'] = True
		self.fields['saldo'].widget.attrs['readonly'] = True

class DetalleDePago2Form(forms.ModelForm):
	class Meta:
		model = DetalleDePago2
		fields = ('__all__')
		widgets = { 
			"cheque": autocomplete.ModelSelect2(url='chequeemitido-autocomplete'),
			"cuenta_bancaria": autocomplete.ModelSelect2(url='cuentabancaria-autocomplete'),
			"monto":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}
