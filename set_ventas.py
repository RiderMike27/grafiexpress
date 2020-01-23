from ventas.models import *

ventas = Venta.objects.all()
for venta in ventas:
	venta.pagado = venta.get_pagado()
	venta.saldo = venta.get_saldo()
	venta.save()
