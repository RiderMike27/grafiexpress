(function($) {
    $(document).ready(function() {

        // recalcular totales al marcar o desmarcar algo como borrado
        $('form input[type=checkbox]').click(function(e) {
            calcular_total();
        });

        // recalcular totales al borrar un factura de un detalle no guardador (con botoncito 'x')
        $('.inline-deletelink').click(function() {
            calcular_total();
        });

        // calcular totales al editar campos numericos
        $('.auto').keyup(function(){
            calcular_total();
        });

        // al cambiar un select en el inline
        $('select').change(function(){
            vector = $(this).attr("id").split("-");

            if( (vector[0] == "id_detalledepago_set") && (vector[2] == "compra") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();

                if(!valueSelected){
                    $("#id_detalledepago_set-" + vector[1] + "-total").val("");
                    $("#id_detalledepago_set-" + vector[1] + "-pagado").val("");
                    $("#id_detalledepago_set-" + vector[1] + "-saldo").val("");
                    $("#id_detalledepago_set-" + vector[1] + "-monto").val("");

                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'compraid' : valueSelected },
                    url : "/admin/compras/getcompra/",
                    type : "get",
                    success : function(data){
                        $("#id_detalledepago_set-" + vector[1] + "-total").val(data[0].total);
                        $("#id_detalledepago_set-" + vector[1] + "-pagado").val(data[0].pagado);
                        $("#id_detalledepago_set-" + vector[1] + "-saldo").val(data[0].saldo);
                        $("#id_detalledepago_set-" + vector[1] + "-monto").val(data[0].saldo);

                        calcular_total();
                    }
                });
            }
        });
    });

})(django.jQuery);

/*
    calculo de los totales
*/
function calcular_total(){
    total_facturas = 0;
    total_forms = $('#id_detalledepago_set-TOTAL_FORMS').val();
    for(i=0;i<total_forms;i++){

        var monto = ($('#id_detalledepago_set-'+i+'-monto').val()!='')?unformat(document.getElementById('id_detalledepago_set-'+i+'-monto')):'0';

        if($('#id_detalledepago_set-'+i+'-DELETE').is(':checked')==false){
            total_facturas += parseFloat(monto)
        }

    }

    $('#id_total_facturas').val( parseFloat(total_facturas).toString().replace(".",",") );
    format(document.getElementById('id_total_facturas'));

    total_medios_de_pago = 0;
    total_forms = $('#id_detalledepago2_set-TOTAL_FORMS').val();
    for(i=0;i<total_forms;i++){

        var monto = ($('#id_detalledepago2_set-'+i+'-monto').val()!='')?unformat(document.getElementById('id_detalledepago2_set-'+i+'-monto')):'0';

        if($('#id_detalledepago2_set-'+i+'-DELETE').is(':checked')==false){
            total_medios_de_pago += parseFloat(monto)
        }

    }

    $('#id_total_medios_de_pago').val( parseFloat(total_medios_de_pago).toString().replace(".",",") );
    format(document.getElementById('id_total_medios_de_pago'));

    $('#id_monto').val( $('#id_total_facturas').val() );
}

