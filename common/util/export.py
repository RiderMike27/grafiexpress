import datetime

from django.http import HttpResponse

import xlwt


#===============================================================================    
#escritor xls   
def listview_to_excel(values_list,name,titulos):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Libro1')
    default_style = xlwt.Style.default_style
    estilo_cabecera = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;'
                          'font: colour white, bold True;')

    for col, datos in enumerate(titulos):
        sheet.write(0, col, datos, style=estilo_cabecera)

    for row, rowdata in enumerate(values_list):
        for col, val in enumerate(rowdata):
            style = default_style
            sheet.write(row+1, col, val, style=style)
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+name+'-'+datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S')+'.xls'
    book.save(response)
    return response

def retiro_detalle_to_excel(lista_datos_central,lista_datos_verdi,nombre_archivo,titulos,titulo_principal):
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('Libro1')
    default_style = xlwt.Style.default_style
    estilo_cabecera = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;'
                          'font: colour white, bold True;')

    row_flag = 0
    col = 0
    
    sheet.write(row_flag, col, titulo_principal, style=default_style)
    
    row_flag += 2
    
    if lista_datos_central:
        sheet.write(row_flag, col, 'Deposito Central', style=estilo_cabecera)
        row_flag += 1
        for col, datos in enumerate(titulos):
            sheet.write(row_flag, col, datos, style=estilo_cabecera)
        row_flag += 1
        for row, rowdata in enumerate(lista_datos_central):
            for col, val in enumerate(rowdata):
                style = default_style
                sheet.write(row_flag+row, col, val, style=style)
        row_flag += row + 2
    


    if lista_datos_verdi:
        col = 0
        sheet.write(row_flag, col, 'Deposito Verdi', style=estilo_cabecera)
        row_flag += 1
        for col, datos in enumerate(titulos):
            sheet.write(row_flag, col, datos, style=estilo_cabecera)
        row_flag += 1
        for row, rowdata in enumerate(lista_datos_verdi):
            for col, val in enumerate(rowdata):
                style = default_style
                sheet.write(row_flag+row, col, val, style=style)
        row_flag += row

    
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+nombre_archivo+'-'+\
                        datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S')+'.xls'
    book.save(response)
    return response

