(function($) {
    $(document).ready(function() {


        $('select').change(function(){
            vector = $(this).attr("id").split("-");

            if( (vector[0] == "id_detalleproduccion_set") && (vector[2] == "detalle_programacion") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();

                if(!valueSelected){
                    $("#id_detalleproduccion_set-" + vector[1] + "-fecha_de_inicio").val("");
                    $("#id_detalleproduccion_set-" + vector[1] + "-hora_de_inicio").val("");
                    $("#id_detalleproduccion_set-" + vector[1] + "-fecha_de_finalizacion").val("");
                    $("#id_detalleproduccion_set-" + vector[1] + "-hora_de_finalizacion").val("");
                    return
                }
                $.ajax({
                    data : {'detalle_programacion_id' : valueSelected },
                    url : "/admin/produccion/getdetalleprogramacion/",
                    type : "get",
                    success : function(data){
                        $("#id_detalleproduccion_set-" + vector[1] + "-fecha_de_inicio").val(data.fecha_de_inicio);
                        $("#id_detalleproduccion_set-" + vector[1] + "-hora_de_inicio").val(data.hora_de_inicio);
                        $("#id_detalleproduccion_set-" + vector[1] + "-fecha_de_finalizacion").val(data.fecha_de_finalizacion);
                        $("#id_detalleproduccion_set-" + vector[1] + "-hora_de_finalizacion").val(data.hora_de_finalizacion);
                    }
                });
            }

        });

    });

})(django.jQuery);



