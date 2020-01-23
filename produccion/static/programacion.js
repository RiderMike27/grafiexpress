(function($) {
    $(document).ready(function() {

        $('.inline-deletelink').click(function() {
            actualizarEntrega();
        });

        $('#detalleprogramacion_set-group').change(function(){
            var rows = $("tr[id*='detalleprogramacion_set']");
            var rows_length = rows.length -1;
            for( var i=0; i<rows_length; i++){
                calcularFinal(i);
            }
        });

        $('select').change(function(){
            vector = $(this).attr("id").split("-");

            if( (vector[0] == "id_detalleprogramacion_set") && (vector[2] == "detalle_proceso") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                if (parseInt(vector[1])>0){
                    var row = parseInt(vector[1])-1;
                    var fecha_anterior = document.getElementById("id_detalleprogramacion_set-" + row + "-fecha_de_finalizacion").value;
                    var hora_anterior = document.getElementById("id_detalleprogramacion_set-" + row + "-hora_de_finalizacion").value;
                }

                if(!valueSelected){
                    $("#id_detalleprogramacion_set-" + vector[1] + "-fecha_de_inicio").val("");
                    return
                }
                $.ajax({
                    data : {'detalle_proceso_id' : valueSelected },
                    url : "/admin/produccion/getdetalleproceso/",
                    type : "get",
                    success : function(data){
                        //En la primera fila se inserta directamente la hora disponible
                        if (parseInt(vector[1])==0){
                            $("#id_detalleprogramacion_set-" + vector[1] + "-fecha_de_inicio").val(data.fecha_de_inicio);
                            $("#id_detalleprogramacion_set-" + vector[1] + "-hora_de_inicio").val(data.hora_de_inicio);
                            $("#id_detalleprogramacion_set-" + vector[1] + "-fecha_de_finalizacion").val(data.fecha_de_finalizacion);
                            $("#id_detalleprogramacion_set-" + vector[1] + "-hora_de_finalizacion").val(data.hora_de_finalizacion);
                            $("#id_detalleprogramacion_set-" + vector[1] + "-pliegos").val(data.pliegos);
                            calcularFinal(vector[1]);
                        } else {
                            //En las siguientes filas, se comparan la hora de finalización del proceso anterior
                            //con la disponibilidad de la maquina
                            //Fecha de finalizacion del proceso anterior
                            var parts = fecha_anterior.split("/");
                            var partsHora = hora_anterior.split(":");
                            var dateProgAnterior = new Date(parseInt(parts[2], 10),
                                              parseInt(parts[1], 10) - 1,
                                              parseInt(parts[0], 10),
                                              parseInt(partsHora[0]));
                            //Fecha disponible de la máquina
                            var partsFechaMaquina = data.fecha_disponible_maquina.split("/");
                            var partsHoraMaquina = data.hora_disponible_maquina.split(":");
                            var dateMaquina = new Date(parseInt(partsFechaMaquina[2], 10),
                                              parseInt(partsFechaMaquina[1], 10) - 1,
                                              parseInt(partsFechaMaquina[0], 10),
                                              parseInt(partsHoraMaquina[0]));
                            if (dateMaquina > dateProgAnterior){
                                $("#id_detalleprogramacion_set-" + vector[1] + "-fecha_de_inicio").val(data.fecha_disponible_maquina);
                                $("#id_detalleprogramacion_set-" + vector[1] + "-hora_de_inicio").val(data.hora_disponible_maquina);
                                $("#id_detalleprogramacion_set-" + vector[1] + "-pliegos").val(data.pliegos);
                            } else {
                                $("#id_detalleprogramacion_set-" + vector[1] + "-fecha_de_inicio").val(data.fecha_de_inicio);
                                $("#id_detalleprogramacion_set-" + vector[1] + "-hora_de_inicio").val(data.hora_de_inicio);
                                $("#id_detalleprogramacion_set-" + vector[1] + "-fecha_de_finalizacion").val(data.fecha_de_finalizacion);
                                $("#id_detalleprogramacion_set-" + vector[1] + "-hora_de_finalizacion").val(data.hora_de_finalizacion);
                                $("#id_detalleprogramacion_set-" + vector[1] + "-pliegos").val(data.pliegos);
                            }
                            calcularFinal(vector[1]);
                        }
                    }
                });
            }

            actualizarEntrega();

        });

    });

})(django.jQuery);

function calcularFinal(indice){
    var texto_id_pliegos = "id_detalleprogramacion_set-" + indice + "-pliegos";
    var pliegos = document.getElementById(texto_id_pliegos).value;
    var texto_id_duracion = "id_detalleprogramacion_set-" + indice + "-duracion";
    var duracion = document.getElementById(texto_id_duracion).value;
    var fecha_id = "id_detalleprogramacion_set-" + indice + "-fecha_de_inicio";
    var fecha = document.getElementById(fecha_id).value;
    var hora_id = "id_detalleprogramacion_set-" + indice + "-hora_de_inicio";
    var hora = document.getElementById(hora_id).value;

    //Transformación de fecha y horas en array de enteros para crear fecha y hora en formato date
    var parts = fecha.split("/");
    var partsHora = hora.split(":");

    var horas_de_trabajo = Math.ceil(duracion);

    //Obtención de hora de finalización
    var hora_sumada = parseInt(partsHora[0]) + horas_de_trabajo;

    if (horas_de_trabajo >= 12){
        horas_de_trabajo = hora_sumada - 9;
    } else if (horas_de_trabajo < 12){
        horas_de_trabajo = hora_sumada - 8;
    }

    var date = new Date(parseInt(parts[2], 10),
                        parseInt(parts[1], 10) - 1,
                        parseInt(parts[0], 10),
                        hora_sumada);
    var buscar = 1;
    var delta = 0;
    while (buscar){
        date.setDate(date.getDate() + delta);
        var numero_de_dia = date.getDay();
        if (numero_de_dia >= 1 && numero_de_dia <= 5){
            if (horas_de_trabajo >= 8){
                horas_de_trabajo -= 8;
                delta += 1;
            } else {
                buscar = 0;
            }
        } else if (numero_de_dia == 6){
            if (horas_de_trabajo >= 4){
                horas_de_trabajo -= 4;
                delta += 2;
            } else {
                buscar = 0;
            }
        } else if (numero_de_dia == 0 && horas_de_trabajo > 0) {
            delta += 1;
        } else {
            buscar = 0;
        }
    }
    var horaString = '';
    if (horas_de_trabajo >= 4){
        horas_de_trabajo += 9;
        horaString = horas_de_trabajo.toString() + ':00';
    }
    else {
        horas_de_trabajo += 8;
        horaString = horas_de_trabajo.toString() + ':00';
    }
    $("#id_detalleprogramacion_set-" + indice + "-fecha_de_finalizacion").val(date.toLocaleDateString());
    $("#id_detalleprogramacion_set-" + indice + "-hora_de_finalizacion").val(horaString);
    $("#id_fecha_de_entrega").val(date.toLocaleDateString());
}

function actualizarEntrega(){
    var rows = $("tr[id*='detalleprogramacion_set']");
    var rows_length = rows.length -1; // para evadir el empty
    var ultima_fecha = document.getElementById("id_detalleprogramacion_set-" + (rows_length-1) + "-fecha_de_finalizacion").value;
    $("#id_fecha_de_entrega").val(ultima_fecha);
}