(function($) {
$(document).ready(function () {
    clientedecontacto();
    $("#id_contacto").change(function () {
        clientedecontacto();
    })
});

function clientedecontacto() {
    var cliente_id_field = $("#id_cliente_id");
    var cliente_field = $("#id_cliente");
    var contacto_id = $("#id_contacto").val();
    if(contacto_id === ""){
        cliente_field.val('');
    }else{
        $.ajax({
            data: {'contacto_id': contacto_id},
            url: "/admin/clientes/get_clientedecontacto/",
            type: "get",
            success: function(data){
                cliente_field.val(data.cliente);
                cliente_id_field.val(data.cliente_id);
            }
        })
    }

}
})(django.jQuery);