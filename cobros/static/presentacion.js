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

            if( (vector[0] == "id_detallepresentacion_set") && (vector[2] == "cobro") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();

                if(!valueSelected){
                    $("#id_detallepresentacion_set-" + vector[1] + "-subtotal").val("");

                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'reciboid' : valueSelected },
                    url : "/admin/cobros/getrecibo/",
                    type : "get",
                    success : function(data){
                        $("#id_detallepresentacion_set-" + vector[1] + "-subtotal").val(separarMiles(parseFloat(data.subtotal)));
                        console.log(parseFloat(data.subtotal))
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
    total = 0;
    total_forms = $('#id_detallepresentacion_set-TOTAL_FORMS').val();
    for(var i=0 ; i<total_forms ; i++){

       var subtotal = document.getElementById('id_detallepresentacion_set-'+i+'-subtotal');
       console.log(subtotal.value.toString().split('.').join(''))
       total += parseInt(subtotal.value.toString().split('.').join(''));

    }

   console.log(total)
   $('#id_total').val(separarMiles(total));
}

function separarMiles(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}


