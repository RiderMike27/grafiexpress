#from dal import autocomplete

from django import forms
from datetime import date
from empresas.models import *

class TimbradoForm(forms.ModelForm):
	class Meta:
		model = Timbrado
		exclude = ['activo',]

class TalonarioForm(forms.ModelForm):
	class Meta:
		model = Talonario
		exclude = ['descripcion', 'ultimo_usado', 'fecha_de_creacion', 'agotado']

	def __init__(self, *args, **kwargs):
		super(TalonarioForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			if(instance.ultimo_usado != None):
				self.fields['numero_inicial'].widget.attrs['readonly'] = True
				self.fields['numero_final'].widget.attrs['readonly'] = True
				self.fields['codigo_de_establecimiento'].widget.attrs['readonly'] = True
				self.fields['punto_de_expedicion'].widget.attrs['readonly'] = True
				self.fields['tipo_de_talonario'].widget.attrs['readonly'] = True
				self.fields['sucursal'].widget.attrs['readonly'] = True
				self.fields['timbrado'].widget.attrs['readonly'] = True

	def clean(self):
		cleaned_data = super(TalonarioForm, self).clean()

		activo = cleaned_data.get("activo")
		if activo == True:

			fecha_de_caducidad = cleaned_data.get("fecha_de_caducidad")
			if fecha_de_caducidad:
				if fecha_de_caducidad < date.today():
					msg = "No se puede poner como activo un talonario vencido, revisar campo fecha de caducidad"
					self.add_error('activo', msg)

		tipo_de_talonario = cleaned_data.get("tipo_de_talonario")
		if tipo_de_talonario != RECIBO:

			codigo_de_establecimiento = cleaned_data.get("codigo_de_establecimiento")
			if codigo_de_establecimiento == "":
				msg = "Este campo es obligatorio."
				self.add_error('codigo_de_establecimiento', msg)	

			punto_de_expedicion = cleaned_data.get("punto_de_expedicion")
			if punto_de_expedicion == "":
				msg = "Este campo es obligatorio."
				self.add_error('punto_de_expedicion', msg)

			timbrado = cleaned_data.get("timbrado")
			if timbrado == None:
				msg = "Este campo es obligatorio."
				self.add_error('timbrado', msg)

