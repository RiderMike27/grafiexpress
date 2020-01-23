from dal import autocomplete
from django import forms
from cheques.models import *

class ChequeRecibidoForm(forms.ModelForm):
	class Meta:
		model = ChequeRecibido
		fields = ('__all__')
		widgets = { 
			"banco": autocomplete.ModelSelect2(url='banco-autocomplete'),
			"monto":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}


class ChequeEmitidoForm(forms.ModelForm):
	class Meta:
		model = ChequeEmitido
		fields = ('__all__')
		widgets = { 
			"banco": autocomplete.ModelSelect2(url='banco-autocomplete'),
			"monto":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}
