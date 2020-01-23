(function($) {
    $(document).ready(function() {

        $('#id_tipo_de_talonario').change(function(){
            set_visibilidad_campos();
        });

        set_visibilidad_campos();
    });



})(django.jQuery);

/*
    Si el tipo de talonario es RECIBO oculta los campos 
    codigo de establecimiento, punto de expedicion y timbrado.
    Si es cualquier otro valor pone visible
*/
function set_visibilidad_campos(){
    if( $('#id_tipo_de_talonario').val() == 2 ){

        $("#id_codigo_de_establecimiento").val("");
        $("#id_punto_de_expedicion").val("");
        $("#id_timbrado").val("");

        $(".field-codigo_de_establecimiento").hide();
        $(".field-punto_de_expedicion").hide();
        $(".field-timbrado").hide();

    } else {
        $(".field-codigo_de_establecimiento").show();
        $(".field-punto_de_expedicion").show();
        $(".field-timbrado").show();
    }
}

