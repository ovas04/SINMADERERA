$(document).ready(function(){
	$(".empleados").addClass("active");
	list_actividad();
});

function list_actividad(){
	$("#tab_actividades").DataTable({
		"aprocessing": true,
		"aServerSide": true,
		"language": {
			"url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/Spanish.json"
		},
		"ajax": {
			"url": "/list_construc_priv",
			"dataSrc": ""
		},
		"columns":[
			{"data":"0"},
			{"data":"1"},
			{"data":"2"},
			{"data":"3"},
			{"data":"7"},
			{"data":"8"},
			{"data":"9"}
		],
		"responsive": true,
		"bDestroy": true,
		"iDisplayLength": 10,
		"autoWidth": false
	});
}