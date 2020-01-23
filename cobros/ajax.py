from django.http.response import JsonResponse

from cobros.models import Recibo


def get_recibo(request):
    recibo_id = (request.GET['reciboid']).replace(" ", "")
    datos = {}

    if recibo_id == "":
        return JsonResponse(datos)

    recibo = Recibo.objects.get(pk=recibo_id)
    datos.update({'subtotal': int(recibo.monto)})

    return JsonResponse(datos)
