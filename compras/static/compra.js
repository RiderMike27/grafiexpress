(function($) {
    $(document).ready(function() {

        // recalcular totales al marcar o desmarcar algo como borrado
        $('form input[type=checkbox]').click(function(e) {
            calcular_total();
        });

        // recalcular totales al borrar un receta de un detalle no guardador (con botoncito 'x')
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

            if(vector[0] == "id_proveedor"){
                                    var optionSelected = $(this).find("option:selected");
                                    var valueSelected  = optionSelected.val();
                                    if(!valueSelected){
                                        $("#id_telefono").val("");
                                        $("#id_contacto").val("");
                                        //$("#id_condicion_de_compra").val("");
                                        return
                                    }
                                    $.ajax({
                                        data : {'proveedorid' : valueSelected },
                                        url : "/admin/proveedores/getproveedor",
                                        type : "get",
                                        success : function(data){
                                            $("#id_telefono").val(data[0].telefono);
                                            $("#id_contacto").val(data[0].contacto);
                                            $("#id_condicion").val(data[0].condicion);
                                        }
                                    });
                                }

            if((vector[0] == "id_proveedor") || (vector[0] == 'id_condicion_de_compra' )){
                                    var optionSelected = $('#id_proveedor').find("option:selected");
                                    var valueSelected  = optionSelected.val();

                                    if(!valueSelected){
                                        $('#id_fecha_de_vencimiento').val('');
                                    }
                                    $.ajax({
                                        data : {'proveedor_id' : valueSelected },
                                        url : "/admin/compras/compra/get_plazo_credito/",
                                        type : "get",
                                        success : function(data){
                                            if ($('#id_condicion').val() == 'CR'){
                                                $('#id_fecha_de_vencimiento').val(data.fecha_vencimiento_credito);
                                            }
                                        }
                                    });

                                }

            if( (vector[0] == "id_detallecompra_set") && (vector[2] == "material") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                console.log(valueSelected)
                if(!valueSelected){
                    $("#id_detallecompra_set-" + vector[1] + "-precio_unitario").val("");
                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'materialid' : valueSelected },
                    url : "/admin/materiales/getmaterial/",
                    type : "get",
                    success : function(data){
                        $("#id_detallecompra_set-" + vector[1] + "-precio_unitario").val(data[0].precio);
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
    var total_general = 0;
    
    total_forms = $('#id_detallecompra_set-TOTAL_FORMS').val();
    for(i=0;i<total_forms;i++){

        var cantidad = ($('#id_detallecompra_set-'+i+'-cantidad').val()!='')?unformat(document.getElementById('id_detallecompra_set-'+i+'-cantidad')):'0';
        var precio_unitario = ($('#id_detallecompra_set-'+i+'-precio_unitario').val()!='')?unformat(document.getElementById('id_detallecompra_set-'+i+'-precio_unitario')):'0';

        var subtotal = parseFloat(cantidad)*parseFloat(precio_unitario)

        if( (cantidad!='0') && (precio_unitario!='0') ){
            $('#id_detallecompra_set-'+i+'-subtotal').val( parseFloat(subtotal).toString().replace(".",",") );
            format(document.getElementById('id_detallecompra_set-'+i+'-subtotal'));
        } else {
            $('#id_detallecompra_set-'+i+'-subtotal').val('');
        }

        if($('#id_detallecompra_set-'+i+'-DELETE').is(':checked')==false){
            total_general += subtotal
        }

    }

    total_forms = $('#id_detallecompra2_set-TOTAL_FORMS').val();
    for(i=0;i<total_forms;i++){

        var cantidad = ($('#id_detallecompra2_set-'+i+'-cantidad').val()!='')?unformat(document.getElementById('id_detallecompra2_set-'+i+'-cantidad')):'0';
        var precio_unitario = ($('#id_detallecompra2_set-'+i+'-precio_unitario').val()!='')?unformat(document.getElementById('id_detallecompra2_set-'+i+'-precio_unitario')):'0';

        var subtotal = parseFloat(cantidad)*parseFloat(precio_unitario)

        if( (cantidad!='0') && (precio_unitario!='0') ){
            $('#id_detallecompra2_set-'+i+'-subtotal').val( parseFloat(subtotal).toString().replace(".",",") );
            format(document.getElementById('id_detallecompra2_set-'+i+'-subtotal'));
        } else {
            $('#id_detallecompra2_set-'+i+'-subtotal').val('');
        }

        if($('#id_detallecompra2_set-'+i+'-DELETE').is(':checked')==false){
            total_general += subtotal
        }

    }

    $('#id_total').val( parseFloat(total_general).toString().replace(".",",") );
    format(document.getElementById('id_total'));
}
