import datetime

import xlwt
from decimal import Decimal
from django.http import HttpResponse
from django.template import response

from deposito.constants import TipoMovimiento
from deposito.models import Deposito, DetalleMovimientoDeMateriales
from deposito.servicios import cantidad_material_in_deposito
from materiales.models import CategoriaDeMaterial, Material
from produccion.models import DetalleRetiro
from presupuestos.models import DetalleDelPresupuesto
from produccion.models import RetiroDevolucion


def stock_to_excel(request):
    depositos = Deposito.objects.all()
    supercategorias = CategoriaDeMaterial.objects.exclude(categoria_padre_id__isnull=False)
    stocks = DetalleMovimientoDeMateriales.objects.filter(movimiento__tipo=TipoMovimiento.ALTA).order_by(
        'material', 'movimiento__deposito').distinct('material', 'movimiento__deposito')

    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Hoja 1')
    default_style = xlwt.Style.default_style
    deposito_style = xlwt.Style.easyxf("font: bold on; align: wrap on, vert centre,  horiz centre; pattern: pattern solid, fore_colour light_green; borders: left thin, right thin, top thin, bottom thin")
    cabecera_style = xlwt.Style.easyxf("font: bold on; align: wrap on, vert centre,  horiz centre; borders: left thin, right thin, top thin, bottom thin")
    sheet.col(1).width = 12400
    sheet.col(0).width = 8000
    i = 0
    for deposito in depositos:
        tiene_contenido = False
        for stock in stocks:
            if stock.movimiento.deposito == deposito:
                tiene_contenido = True

        if tiene_contenido:
            sheet.merge(i, i, 0, 3)
            sheet.write(i, 0, deposito.nombre, deposito_style)
            sheet.write(i+1, 0, 'Categoria', cabecera_style)
            sheet.write(i+1, 1, 'Material', cabecera_style)
            sheet.write(i+1, 2, 'Codigo de Material', cabecera_style)
            sheet.write(i+1, 3, 'Cantidad en Stock', cabecera_style)
            sheet.row(i+1).height = 600
            i += 2

        for supercategoria in supercategorias:
            tiene_elementos = False
            for stock in stocks:
                objeto = stock.material.categoria

                while objeto.categoria_padre is not None:
                    objeto = objeto.categoria_padre

                if objeto == supercategoria and stock.movimiento.deposito == deposito:
                    tiene_elementos = True

            if tiene_elementos:
                sheet.write(i, 0, supercategoria.nombre_completo, default_style)
                i += 1
                for stock in stocks:
                    objeto = stock.material.categoria

                    while objeto.categoria_padre is not None:
                        objeto = objeto.categoria_padre
                    if objeto == supercategoria and stock.movimiento.deposito == deposito:
                        cantidad = cantidad_material_in_deposito(deposito, stock.material)
                        sheet.write(i, 1, stock.material.descripcion)
                        sheet.write(i, 2, stock.material.id)
                        sheet.write(i, 3, int(cantidad))
                        i += 1
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + 'Datos Stock' + '-' + datetime.datetime.now().strftime(
        '%Y-%m-%d|%H:%M:%S') + '.xls'
    book.save(response)
    return response


def listado_to_excel():
    supercategorias = CategoriaDeMaterial.objects.exclude(categoria_id__isnull=False)
    productos = Material.objects.filter(tiene_hijo=False).order_by('id')

    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Hoja 1')
    default_style = xlwt.Style.default_style

    i = 0
    for supercategoria in supercategorias:
        tiene_elementos = False
        for producto in productos:
            objeto = producto
            while objeto.categoria != None:
                objeto = objeto.categoria

            if (objeto == supercategoria):
                tiene_elementos = True

        if (tiene_elementos):
            sheet.write(i, 1, supercategoria.nombre)
            i += 1
            for producto in productos:
                objeto = producto
                while objeto.categoria != None:
                    objeto = objeto.categoria
                if (objeto == supercategoria):
                    sheet.write(i, 2, producto.id)
                    sheet.write(i, 3, producto.codigo)
                    sheet.write(i, 4, producto.nombrecompleto)
                    i += 1
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + 'Datos Stock' + '-' + datetime.datetime.now().strftime(
        '%Y-%m-%d|%H:%M:%S') + '.xls'
    book.save(response)
    return response

#ivan caceres
# ejemplo simple que funciona bien
# def retiro_to_excel(request):
#     palabra = 'ivan'
#     book = xlwt.Workbook(encoding='utf8')
#
#     sheet = book.add_sheet('Hoja 1')
#     sheet.write(0, 0, palabra)
#     response = HttpResponse(content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=' + 'Datos Stock' + '-' + datetime.datetime.now().strftime(
#         '%Y-%m-%d|%H:%M:%S') + '.xls'
#     book.save(response)
#     return response

def retiro_to_excel(request):
    retiros = DetalleRetiro.objects.all()

    #ESTO ES LO QUE TIENE DETALLERETIRO
    # retiro = models.ForeignKey(Retiro)
    # orden_de_trabajo = models.ForeignKey(OrdenDeTrabajo, null=True, blank=True)
    # deposito = models.ForeignKey('deposito.Deposito')
    # material = models.ForeignKey("materiales.Material")
    # cantidad = models.DecimalField(max_digits=15, decimal_places=2)

    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Hoja 1')

    default_style = xlwt.Style.default_style
    deposito_style = xlwt.Style.easyxf(
        "font: bold on; align: wrap on, vert centre,  horiz centre; pattern: pattern solid, fore_colour light_green; borders: left thin, right thin, top thin, bottom thin")
    cabecera_style = xlwt.Style.easyxf(
        "font: bold on; align: wrap on, vert centre,  horiz centre; borders: left thin, right thin, top thin, bottom thin")
    cabecera_style2 = xlwt.Style.easyxf(
        "align: wrap on, vert centre,  horiz centre; borders: left thin, right thin, top thin, bottom thin")

    sheet.col(2).width = 4500
    sheet.col(3).width = 4000
    sheet.col(4).width = 4000

    sheet.merge(0, 0, 0, 5)
    sheet.write(0, 0, 'Detalle de los retiros', deposito_style)


    sheet.write(1, 1, 'retiro',cabecera_style)
    sheet.write(1, 2, 'orden de trabajo',cabecera_style)
    sheet.write(1, 3, 'deposito',cabecera_style)
    sheet.write(1, 4, 'material',cabecera_style)
    sheet.write(1, 5, 'cantidad',cabecera_style)
    i = 1


    for retiro in retiros:

        sheet.write(i + 1, 0, i,cabecera_style2)
        sheet.write(i + 1, 1, str(retiro.retiro_id),cabecera_style2)
        a = str(retiro.orden_de_trabajo_id)

        if  a != "None":
            sheet.write(i + 1, 2, str(retiro.orden_de_trabajo_id),cabecera_style2)
        else:
            sheet.write(i + 1, 2, 'no hay',cabecera_style2)
        sheet.write(i + 1, 3, str(retiro.deposito),cabecera_style2)
        sheet.write(i + 1, 4, str(retiro.material),cabecera_style2)
        sheet.write(i + 1, 5, str(retiro.cantidad),cabecera_style2)
        i = i + 1

    sheet.write(1, 0, 'numero',cabecera_style)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + 'Datos Stock' + '-' + datetime.datetime.now().strftime(
        '%Y-%m-%d|%H:%M:%S') + '.xls'
    book.save(response)
    return response


def listado_to_excel_retiro_dev(request):
    ret_dev = RetiroDevolucion.objects.all()

    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Hoja 1')
    default_style = xlwt.Style.default_style
    deposito_style = xlwt.Style.easyxf("font: bold on; align: wrap on, vert centre,  horiz centre; pattern: pattern solid, fore_colour light_green; borders: left thin, right thin, top thin, bottom thin")
    cabecera_style = xlwt.Style.easyxf("font: bold on; align: wrap on, vert centre,  horiz centre; borders: left thin, right thin, top thin, bottom thin")
    sheet.col(1).width = 3000
    sheet.col(0).width = 2000
    sheet.col(4).width = 3000
    sheet.col(5).width = 6000
    sheet.col(6).width = 6000
    sheet.col(7).width = 6000
    sheet.col(10).width = 6000

    sheet.merge(0, 0, 0, 10)
    sheet.write(0, 0, 'RETIROS/DEVOLUCIONES', deposito_style)
    sheet.write(1, 0, 'Cod', cabecera_style)
    sheet.write(1, 1, 'Fecha', cabecera_style)
    sheet.write(1, 2, 'Tipo', cabecera_style)
    sheet.write(1, 3, 'OT', cabecera_style)
    sheet.write(1, 4, 'Presupuesto', cabecera_style)
    sheet.write(1, 5, 'Funcionario', cabecera_style)
    sheet.write(1, 6, 'Deposito', cabecera_style)
    sheet.write(1, 7, 'Material', cabecera_style)
    sheet.write(1, 8, 'Precio Unitario', cabecera_style)
    sheet.write(1, 9, 'Cantidad', cabecera_style)
    sheet.write(1, 10, 'Subtotal', cabecera_style)

    sheet.row(1).height = 600

    i = 2
    for retiros_devoluciones in ret_dev:
        def tipo(obj):
            if obj.retiro_id:
                return 'RETIRO'
            else:
                return 'DEVOLUCION'
        def presupuesto(obj):
            detalle_presupuesto = DetalleDelPresupuesto.objects.filter(item=obj.orden_de_trabajo.item_presupuesto)
            if detalle_presupuesto.exists():
                detalle_presupuesto = detalle_presupuesto.get()
                presu_nombre = detalle_presupuesto.presupuesto.nombre_del_trabajo
            return presu_nombre
        presunombre = presupuesto(retiros_devoluciones)
        tipo_RD = tipo(retiros_devoluciones)

        def subtotal(obj):
            return "%.2f" % Decimal(obj.cantidad * obj.precio_unitario)
        subtot = subtotal(retiros_devoluciones)
        def codigo( obj):
            if obj.retiro_id:
                return obj.retiro_id
            else:
                return obj.devolucion_id
        id = codigo(retiros_devoluciones)
        sheet.write(i, 0, id)
        sheet.write(i, 1, retiros_devoluciones.fecha.__str__())
        sheet.write(i, 2, tipo_RD)
        sheet.write(i, 3, retiros_devoluciones.orden_de_trabajo.__str__())
        sheet.write(i, 4, presunombre)
        sheet.write(i, 5, retiros_devoluciones.funcionario.__str__())
        sheet.write(i, 6, retiros_devoluciones.deposito.__str__())
        sheet.write(i, 7, retiros_devoluciones.material.__str__())
        sheet.write(i, 8, retiros_devoluciones.precio_unitario.__str__())
        sheet.write(i, 9, retiros_devoluciones.cantidad.__str__())
        sheet.write(i, 10, subtot)
        i += 1

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + 'Retiros/Devoluciones' + '-' + datetime.datetime.now().strftime(
        '%Y-%m-%d|%H:%M:%S') + '.xls'
    book.save(response)

    return response
