from django.contrib import admin
from django.contrib.admin.decorators import register
from empresas.models import *
from empresas.forms import *

# Register your models here.

class SucursalInlineAdmin(admin.StackedInline):
	model = Sucursal
	extra = 1

@register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
	change_form_template = 'empresa_form.html'

	inlines = [ SucursalInlineAdmin, ]


@register(Talonario)
class TalonarioAdmin(admin.ModelAdmin):
	class Media:
		js = ('talonario.js',)

	form = TalonarioForm


@register(Timbrado)
class Timbrado(admin.ModelAdmin):
	pass

