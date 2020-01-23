# -*- coding: utf-8 -*-


class TipoProceso:
    IMPRESION = 'impresion'
    PLASTIFICADO = 'plastificado'
    TROQUEL_FABRICACION = 'troquel_fabricacion'
    TROQUELADO = 'toquelado'
    TERMINACION = 'terminacion'
    TERCERIZADO = 'tercerizado'
    EMPAQUETADO = 'empaquetado'
    EMPLACADO = 'emplacado'
    DOBLADO = 'doblado'
    PEGADO = 'pegado'
    COSIDO = 'cosido'

    TIPOS = (
        (IMPRESION, 'Impresión'),
        (PLASTIFICADO, 'Plastificado'),
        (TROQUEL_FABRICACION, 'Troquel Fabricación'),
        (TROQUELADO, 'Troquelado'),
        (TERMINACION, 'Terminación'),
        (TERCERIZADO, 'Tercerizado'),
        (EMPAQUETADO, 'Empaquetado'),
        (EMPLACADO, 'Emplacado'),
        (DOBLADO, 'Doblado'),
        (PEGADO, 'Pegado'),
        (COSIDO, 'Cosido'),
    )


class EstadoProceso:
    NO_INICIADO = 'no_iniciado'
    EN_PROCESO = 'en_proceso'
    FINALIZADO = 'finalizado'

    ESTADOS = (
        (NO_INICIADO, 'No iniciado'),
        (EN_PROCESO, 'En proceso'),
        (FINALIZADO, 'Finalizado')
    )