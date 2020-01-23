import json
from django.http import HttpResponse
from maquinaria.models import *
from extra.globals import separador_de_miles


def get_maquina(request):
    maquina_id = (request.GET['maquinaid']).replace(" ","")

    result_set = []

    if maquina_id == "":
        return HttpResponse(json.dumps(result_set), 
                            content_type='application/json')

    maquina = Maquina.objects.get(pk = maquina_id)

    result_set.append({
        'descripcion': maquina.descripcion,
        'precio': separador_de_miles(maquina.precio),
        'codigo': maquina.id
    })

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')
