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

            if(vector[0] == "id_talonario"){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                console.log(valueSelected)
                if(!valueSelected){
                    $("#id_numero").val("");
                    return
                }
                $.ajax({
                    data : {'talonarioid' : valueSelected },
                    url : "/admin/empresas/gettalonario/",
                    type : "get",
                    success : function(data){
                        $("#id_numero").val(data[0].numero);
                    }
                });
            }


            if( (vector[0] == "id_detallederecibo_set") && (vector[2] == "factura") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();

                if(!valueSelected){
                    $("#id_detallederecibo_set-" + vector[1] + "-total").val("");
                    $("#id_detallederecibo_set-" + vector[1] + "-pagado").val("");
                    $("#id_detallederecibo_set-" + vector[1] + "-saldo").val("");
                    $("#id_detallederecibo_set-" + vector[1] + "-monto").val("");

                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'ventaid' : valueSelected },
                    url : "/admin/ventas/getventa/",
                    type : "get",
                    success : function(data){
                        $("#id_detallederecibo_set-" + vector[1] + "-total").val(data[0].total);
                        $("#id_detallederecibo_set-" + vector[1] + "-pagado").val(data[0].pagado);
                        $("#id_detallederecibo_set-" + vector[1] + "-saldo").val(data[0].saldo);
                        $("#id_detallederecibo_set-" + vector[1] + "-monto").val(data[0].saldo);

                        calcular_total();
                    }
                });
            }
        });

        $('#detallederecibo2_set-group').change(function(){
            calcular_total();
        });
    });

})(django.jQuery);

/*
    calculo de los totales
*/
function calcular_total(){
    total_facturas = 0;
    total_forms = $('#id_detallederecibo_set-TOTAL_FORMS').val();
    for(var i=0;i<total_forms;i++){

        var monto = ($('#id_detallederecibo_set-'+i+'-monto').val()!='')?unformat(document.getElementById('id_detallederecibo_set-'+i+'-monto')):'0';

        if($('#id_detallederecibo_set-'+i+'-DELETE').is(':checked')==false){
            total_facturas += parseFloat(monto)
        }

    }

    $('#id_total_facturas').val( parseFloat(total_facturas).toString().replace(".",",") );
    format(document.getElementById('id_total_facturas'));

    total_medios_de_pago = 0;
    total_forms = $('#id_detallederecibo2_set-TOTAL_FORMS').val();
    for(var i=0; i<total_forms; i++){
        var cheque_id = $('#id_detallederecibo2_set-'+i+'-cheque').val();

        if (cheque_id != null){
            $.ajax({
                    data : {'cheque_id' : cheque_id },
                    url : "/admin/cheques/get_monto_cheque_recibido/",
                    type : "get",
                    async: false,
                    success : function(data){
                        $('#id_detallederecibo2_set-'+i+'-monto').val(data[0].monto);
                    }
                });
        }

        var monto = ($('#id_detallederecibo2_set-'+i+'-monto').val()!='')?unformat(document.getElementById('id_detallederecibo2_set-'+i+'-monto')):'0';

        if($('#id_detallederecibo2_set-'+i+'-DELETE').is(':checked')==false){
            total_medios_de_pago += parseFloat(monto)
        }

    }

    $('#id_total_medios_de_pago').val( parseFloat(total_medios_de_pago).toString().replace(".",",") );
    format(document.getElementById('id_total_medios_de_pago'));

    $('#id_monto').val( $('#id_total_facturas').val() );
}

