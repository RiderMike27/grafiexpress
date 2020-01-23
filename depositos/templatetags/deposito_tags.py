from django import template
from materiales.models import Material
from depositos.models import Deposito

register = template.Library()

@register.assignment_tag
def get_stock_material_deposito(material_id, deposito_id):
	material = Material.objects.get(pk=material_id)
	return material.get_stock_deposito(deposito_id=deposito_id)