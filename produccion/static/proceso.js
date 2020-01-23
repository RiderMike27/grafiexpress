(function($) {
    $(document).ready(function() {

        $("#id_pliegos").change(function () {
            var cantidad = document.getElementById('id_pliegos').value;
            populatePliegos(cantidad)
            });

        $('.inline-deletelink').click(function() {
            actualizarEntrega();
        });

        $('#detalleproceso_set-group').change(function(){
            var rows = $("tr[id*='detalleproceso_set']");
            var rows_length = rows.length -1;
            for( var i=0; i<rows_length; i++){
                calcularFinal(i);
            }
        });

        $('select').change(function(){
            vector = $(this).attr("id").split("-");

            if( (vector[0] == "id_detalleproceso_set") && (vector[2] == "maquina") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                if (parseInt(vector[1])>0){
                    var row = parseInt(vector[1])-1;
                    var fecha_anterior = document.getElementById("id_detalleproceso_set-" + row + "-fecha_de_finalizacion").value;
                    var hora_anterior = document.getElementById("id_detalleproceso_set-" + row + "-hora_de_finalizacion").value;
                }

                if(!valueSelected){
                    $("#id_detalleproceso_set-" + vector[1] + "-fecha_de_inicio").val("");
                    return
                }
                $.ajax({
                    data : {'maquina_id' : valueSelected },
                    url : "/admin/produccion/getmaquina/",
                    type : "get",
                    success : function(data){
                        //En la primera fila se inserta directamente la hora disponible de la máquina
                        if (parseInt(vector[1])==0){
                            $("#id_detalleproceso_set-" + vector[1] + "-pasadas_por_hora").val(data.pasadas_por_hora);
                            $("#id_detalleproceso_set-" + vector[1] + "-fecha_de_inicio").val(data.fecha_disponible);
                            $("#id_detalleproceso_set-" + vector[1] + "-hora_de_inicio").val(data.hora_disponible);
                            $("#id_detalleproceso_set-" + vector[1] + "-tercerizado").val(data.tercerizado);
                            $("#id_detalleproceso_set-" + vector[1] + "-pliegos_a_realizar").val(document.getElementById('id_pliegos').value);
                            calcularFinal(vector[1]);
                        } else {
                            //En las siguientes filas, se comparan la hora de finalización del proceso anterior con la hora de la máquina

                            //Fecha de finalizacion del proceso anterior
                            var parts = fecha_anterior.split("/");
                            var partsHora = hora_anterior.split(":");
                            var dateProcAnterior = new Date(parseInt(parts[2], 10),
                                              parseInt(parts[1], 10) - 1,
                                              parseInt(parts[0], 10),
                                              parseInt(partsHora[0]));
                            //Fecha disponible de la máquina
                            var partsFechaMaquina = data.fecha_disponible.split("/");
                            var partsHoraMaquina = data.hora_disponible.split(":");
                            var dateMaquina = new Date(parseInt(partsFechaMaquina[2], 10),
                                              parseInt(partsFechaMaquina[1], 10) - 1,
                                              parseInt(partsFechaMaquina[0], 10),
                                              parseInt(partsHoraMaquina[0]));
                            if (dateMaquina > dateProcAnterior){
                                $("#id_detalleproceso_set-" + vector[1] + "-pasadas_por_hora").val(data.pasadas_por_hora);
                                $("#id_detalleproceso_set-" + vector[1] + "-fecha_de_inicio").val(data.fecha_disponible);
                                $("#id_detalleproceso_set-" + vector[1] + "-hora_de_inicio").val(data.hora_disponible);
                                $("#id_detalleproceso_set-" + vector[1] + "-tercerizado").val(data.tercerizado);
                                $("#id_detalleproceso_set-" + vector[1] + "-pliegos_a_realizar").val(document.getElementById('id_pliegos').value);
                            } else {
                                $("#id_detalleproceso_set-" + vector[1] + "-pasadas_por_hora").val(data.pasadas_por_hora);
                                $("#id_detalleproceso_set-" + vector[1] + "-fecha_de_inicio").val(fecha_anterior);
                                $("#id_detalleproceso_set-" + vector[1] + "-hora_de_inicio").val(hora_anterior);
                                $("#id_detalleproceso_set-" + vector[1] + "-tercerizado").val(data.tercerizado);
                                $("#id_detalleproceso_set-" + vector[1] + "-pliegos_a_realizar").val(document.getElementById('id_pliegos').value);
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

function populatePliegos(cantidad){
    var rows = $("tr[id*='detalleproceso_set']");
    var rows_length = rows.length -1; // para evadir el empty

    for( var i=0; i<rows_length; i++){
        $('#id_detalleproceso_set-'+i+'-pliegos_a_realizar').val(parseInt(cantidad));
    }
}

function calcularFinal(indice){
    var texto_id_pliegos = "id_detalleproceso_set-" + indice + "-pliegos_a_realizar";
    var pliegos = document.getElementById(texto_id_pliegos).value;
    var texto_id_pasadas = "id_detalleproceso_set-" + indice + "-pasadas_por_pliego";
    var pasadas_por_pliego = document.getElementById(texto_id_pasadas).value;
    var texto_id_pasadas_hora = "id_detalleproceso_set-" + indice + "-pasadas_por_hora";
    var pasadas_por_hora = document.getElementById(texto_id_pasadas_hora).value;
    var texto_id_tercerizado = "id_detalleproceso_set-" + indice + "-tercerizado";
    var tercerizado = document.getElementById(texto_id_tercerizado).value;
    //Obtención de datos para calculo de total de horas de trabajo
    var total_pasadas = pliegos*pasadas_por_pliego;
    var horas_de_trabajo = Math.ceil(total_pasadas/pasadas_por_hora);

    //Obtención de fecha y hora de inicio establecidos
    var fecha_id = "id_detalleproceso_set-" + indice + "-fecha_de_inicio";
    var fecha = document.getElementById(fecha_id).value;
    var hora_id = "id_detalleproceso_set-" + indice + "-hora_de_inicio";
    var hora = document.getElementById(hora_id).value;
    var horas_por_dia_id = "id_detalleproceso_set-" + indice + "-horas_por_dia";
    var horas_por_dia = document.getElementById(horas_por_dia_id).value;
    var media_jornada = Math.ceil(horas_por_dia/2);

    //Transformación de fecha y horas en array de enteros para crear fecha y hora en formato date
    var parts = fecha.split("/");
    var partsHora = hora.split(":");

    //Obtención de hora de finalización
    var hora_sumada = parseInt(partsHora[0]) + horas_de_trabajo;
    // Correccion de hora, introduciendo hora de descanso pasado el mediodia
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
            if (horas_de_trabajo >= horas_por_dia){
                horas_de_trabajo -= horas_por_dia;
                delta += 1;
            } else {
                buscar = 0;
            }
        } else if (numero_de_dia == 6){
            if (horas_de_trabajo >= media_jornada){
                horas_de_trabajo -= media_jornada;
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
    if(tercerizado!='1'){
        $("#id_detalleproceso_set-" + indice + "-fecha_de_finalizacion").val(date.toLocaleDateString());
        $("#id_detalleproceso_set-" + indice + "-hora_de_finalizacion").val(horaString);
        $("#id_fecha_de_entrega").val(date.toLocaleDateString());
    }
}

function actualizarEntrega(){
    var rows = $("tr[id*='detalleproceso_set']");
    var rows_length = rows.length -1; // para evadir el empty
    var ultima_fecha = document.getElementById("id_detalleproceso_set-" + (rows_length-1) + "-fecha_de_finalizacion").value;
    $("#id_fecha_de_entrega").val(ultima_fecha);
}