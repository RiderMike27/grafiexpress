from django.http.response import HttpResponse
import json
from depositos.templatetags.deposito_tags import get_stock_material_deposito as get_stock

from extra.globals import separador_de_miles

from django.http import JsonResponse

def get_stock_material_deposito(request):
    material_id = request.GET.get('material_id','')
    deposito_id = request.GET.get('deposito_id','')
    datos = {
        'saldo':  separador_de_miles(get_stock(material_id=material_id,deposito_id=deposito_id))
    }

    return JsonResponse(datos)
