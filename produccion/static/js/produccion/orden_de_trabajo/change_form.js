function get_vendedor()
{
	ajaxGet('/produccion/ajax/get_vendedor',
			{cliente: String($('#id_cliente').val())},
			function(content)
	{
        $('#vendedor_nombre').html(content);
	})
}

function check_cambios()
{
	if($('#id_cambios').is(":checked"))
	{
		var total = parseInt($("#id_detalleordendetrabajo_set-TOTAL_FORMS").val());
		$("#detalleordendetrabajo_set-0").parent().find(".add-row").show();
		
		for (var i=0; i<total; i++)
		{
			$("#detalleordendetrabajo_set-" + String(i+1)).show();
		}
	}
	else
	{
		var total = parseInt($("#id_detalleordendetrabajo_set-TOTAL_FORMS").val());
		
		$("#detalleordendetrabajo_set-0").parent().find(".add-row").hide();
		
		for (var i=0; i<total; i++)
		{	
			if ($("#id_detalleordendetrabajo_set-" + String(i+1) + "-DELETE").length)	//Check if check exists
			{
				$("#id_detalleordendetrabajo_set-" + String(i+1) + "-DELETE").attr('checked', true);
			}
			else
			{
				$("#detalleordendetrabajo_set-" + String(i+1)).find("input").val("");
				$("#detalleordendetrabajo_set-" + String(i+1)).find("select").val("");
			}
			$("#detalleordendetrabajo_set-" + String(i+1)).hide();
		}
	}
}

function thousand_separators(x)
{
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function update_total()
{
	var precio = $("#id_precio_unitario").val();
    var cantidad = $("#id_cantidad").val();
    
    console.log(precio);
    console.log(cantidad);
	
	if (precio != "" && cantidad != "")
	{
		var s = thousand_separators(String(Math.round(parseFloat(precio) * parseFloat(cantidad))));
		$("#detalles_total").html(s);
	}
}

$(document).ready(function()
{
	get_vendedor();
	check_cambios();
	
	if ($('#id_numero').val() == '')
	{
		ajaxGet('/produccion/ajax/get_next_orden_de_trabajo_id',
				function(content)
		{
	        $('#id_numero').val(String(content));
		});
	}
	
	$("#id_cliente").change(get_vendedor);
	$('#id_cambios').change(check_cambios);
	
	$("#id_precio_unitario").change(update_total);
	$("#id_cantidad").change(update_total);
});
