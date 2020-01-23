from deposito.models import Deposito, DetalleMovimientoDeMateriales
from deposito.servicios import cantidad_material_in_deposito
from materiales.models import CategoriaDeMaterial, Material


def stock_to_excel2(request):
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


def listado_to_excel2():
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
