$(document).ready(function(){
	$(".s-construcciones").css("display","block");
	$(".construcciones").addClass("active");
	$(".priv").addClass("active");
	list_construc();
	regis_construc();
	ver_construc();
	edit_construc();
	eli_construc();
});

function list_construc(){
	$("#tab_constructoras").DataTable({
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
			{"data":"4"},
			{"data":"5"},
			{"data":"6"},
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

function regis_construc(){
	var form = document.querySelector("#form-construc");
	$(".btn-form").click(function(e){
		e.preventDefault();
		var request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
		var ajaxUrl = "/regis_construc_priv";
		var formData = new FormData(form);
		request.open("POST",ajaxUrl,true);
		request.send(formData);
		request.onload = function(){
			if(request.status == 200){
				var objData = JSON.parse(request.responseText);
				if(objData.status){
					$("#modal-construc").modal("hide");
					form.reset();
					Swal.fire("¡Registrado!",objData.msg,"success");
					$("#tab_constructoras").DataTable().ajax.reload();
				}else{
					Swal.fire("¡Error!",objData.msg,"error");
				}
			}else{
				console.log("No se enviaron los datos");
			}
		}
	});
}

function ver_construc(){
	$("#tab_constructoras").on("click",".btn-ver-construc",function(){
		$("#modal-det-construc").modal("show");
		var id_construc = this.getAttribute("rl");
		var request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
		var ajaxUrl = "/buscar_construc_priv/"+id_construc;
		request.open("GET",ajaxUrl,true);
		request.send();
		request.onload = function(){
			if(request.status == 200){
				var objData = JSON.parse(request.responseText);
				$("#id_construc_d").val(id_construc);
				$("#nom_construc_d").val(objData[1]);
				$("#ubi_construc_d").val(objData[2]);
				$("#dir_construc_d").val(objData[3]);
				$("#tipo_d").val(objData[4]);
				$("#fech_entrega_d").val(objData[6]);
				$("#constructora_d").val(objData[7]);
				$("#etapa_d").val(objData[5]);
				$("#descri_d").val(objData[9]);
				$("#financ_d").val(objData[10]);
				$("#estado_d").val(objData[8]);
			}
		}
	});
}

function edit_construc(){
	$("#tab_constructoras").on("click",".btn-edit-construc",function(){
		$("#modal-construc .btn-form").removeClass("btn-success").addClass("btn-primary");
		$("#modal-construc .modal-title").text("Actualizar Construcción")
		$("#modal-construc .btn-text").text("Actualizar");
		$("#modal-construc").modal("show");
		var id_construc = this.getAttribute("rl");
		var request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
		var ajaxUrl = "/buscar_construc_priv/"+id_construc;
		request.open("GET",ajaxUrl,true);
		request.send();
		request.onload = function(){
			if(request.status == 200){
				var objData = JSON.parse(request.responseText);
				$("#id_construc").val(id_construc);
				$("#nom_construc").val(objData[1]);
				$("#ubi_construc").val(objData[2]);
				$("#dir_construc").val(objData[3]);
				$("#tipo").val(objData[4]);
				$("#fech_entrega").val(objData[6]);
				$("#constructora").val(objData[7]);
				$("#etapa").val(objData[5]);
				$("#descri").val(objData[9]);
				$("#financ").val(objData[10]);
				$("#estado").val(objData[8]);
			}
		}
	});
}

function eli_construc(){
	$("#tab_constructoras").on("click",".btn-eli-construc",function(){
		var id_construc = this.getAttribute("rl");
		Swal.fire({
			title: "Eliminar Construccion",
			text: "¿Desea eliminar esta construccion?",
			icon: "question",
			showCancelButton: true,
			confirmButtonText: "Si, eliminar!",
			cancelButtonText: "No, cancelar!"
		}).then((result)=>{
			if(result.isConfirmed){
				var request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
				var ajaxUrl = "/elim_construc_priv/"+id_construc;
				request.open("POST",ajaxUrl,true);
				request.send();
				request.onload = function(){
					if(request.status == 200){
						var objData = JSON.parse(request.responseText);
						Swal.fire("¡Eliminado!",objData.msj,"success");
						$("#tab_constructoras").DataTable().ajax.reload();
					}else{
						Swal.fire("Construcciones","El registro no pudo ser eliminado","error");
					}
				}
			}else{
				Swal.fire("Cancelado","Tu registro está seguro :)","error");
			}
		});
	});
}

function open_modal(){
	$("#modal-construc .btn-form").removeClass("btn-primary").addClass("btn-success");
	$("#modal-construc .modal-title").text("Registrar Construcción")
	$("#modal-construc .btn-text").text("Registrar");
	$("#modal-construc").modal("show");
	$("#id_construc").val("0");
	$("#form-construc")[0].reset();
}