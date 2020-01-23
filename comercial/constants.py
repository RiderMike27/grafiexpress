# -*- coding: utf-8 -*-


class EstadoPresupuestos:
    PENDIENTE = 'pen'
    PRESUPUESTADO = 'pre'
    ENVIADO = 'env'

    ESTADOS = (
        (PENDIENTE, 'Pendiente'),
        (PRESUPUESTADO, 'Presupuestado'),
        (ENVIADO, 'Enviado al cliente'),
    )
