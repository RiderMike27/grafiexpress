from dal import autocomplete
from django import forms
from bancos.models import CuentaBancaria

class CuentaBancariaForm(forms.ModelForm):
	class Meta:
		model = CuentaBancaria
		fields = ('__all__')
		widgets = { 
			"banco": autocomplete.ModelSelect2(url='banco-autocomplete'),
		}
