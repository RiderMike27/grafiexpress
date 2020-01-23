from produccion.models import OrdenDeTrabajo

ots = OrdenDeTrabajo.objects.all()
for ot in ots:
	ot.actualizar_cantidades()

