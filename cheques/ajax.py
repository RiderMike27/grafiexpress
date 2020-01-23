import json
from django.http import HttpResponse

from cheques.models import ChequeRecibido


def get_monto_cheque_recibido(request):
    cheque_id = int(request.GET['cheque_id'])

    result_set = []

    if cheque_id:
        monto = float((ChequeRecibido.objects.get(pk=cheque_id)).monto)
        result_set.append({
            'monto': monto,
        })

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')
