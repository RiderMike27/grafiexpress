from dal import autocomplete
from django import forms
from maquinaria.models import Maquina

class MaquinaForm(forms.ModelForm):
	class Meta:
		model = Maquina
		fields = ('__all__')
		widgets = { "precio":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
					}