function thousand_separators(x)
{
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function update_orden_de_trabajo_data()
{
	var dot_id = $("#id_detalle_orden_de_trabajo").val();
	
	ajaxGet('/produccion/ajax/costo/get_details',
			{dot_id: String(dot_id)},
			function(content)
			{
		        $("#ot_nombre").html(content.nombre);
		        $("#ot_cliente").html(content.cliente);
		        $(".ot_cantidad").html(thousand_separators(content.cantidad));
		        $("#ot_presupuesto").html(content.presupuesto);
		        $("#ot_fecha").html(content.fecha);
		        $("#ot_vendedor").html(content.vendedor);
		        
		        $("#ot_papel").html(content.papel);
		        $("#ot_gramaje").html(content.gramaje);
		        $("#ot_precio_unitario").html(thousand_separators(content.precio_unitario));
		        $("#ot_total").html(thousand_separators(content.precio_unitario * content.cantidad));
			});
}

$(document).ready(function()
{
	update_orden_de_trabajo_data();
	
	$("#id_detalle_orden_de_trabajo").change(update_orden_de_trabajo_data);
});
