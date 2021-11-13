$(document).ready(function(){
    $(".s-usuarios").css("display","block");
    $(".usuarios").addClass("active");
    edit_usuario();
    eli_usuario();
});

function list_usuario(){
	$("#tab_usuarios").DataTable({
		"aprocessing": true,
		"aServerSide": true,
		"language": {
			"url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/Spanish.json"
		},
		"ajax": {
			"url": "/list_usuarios",
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
			{"data":"7"}
		],
		"responsive": true,
		"bDestroy": true,
		"iDisplayLength": 10,
		"autoWidth": false
	});
}

function regis_usuario(){
	var form = document.querySelector("#form-usuario");
	$(".btn-form").click(function(e){
		e.preventDefault();
		var request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
		var ajaxUrl = "/regis_usuario";
		var formData = new FormData(form);
		request.open("POST",ajaxUrl,true);
		request.send(formData);
		request.onload = function(){
			if(request.status == 200){
				var objData = JSON.parse(request.responseText);
				if(objData.status){
					$("#modal-usuario").modal("hide");
					form.reset();
					Swal.fire("¡Registrado!",objData.msg,"success");
					$("#tab_usuarios").DataTable().ajax.reload();
				}else{
					Swal.fire("¡Error!",objData.msg,"error");
				}
			}else{
				console.log("No se enviaron los datos");
			}
		}
	});
}

function edit_usuario(){
	$("#tab_usuarios").on("click",".btn-edit-usu",function(){
		$("#modal-usuario .btn-form").removeClass("btn-success").addClass("btn-primary");
		$("#modal-usuario .modal-title").text("Actualizar Usuario")
		$("#modal-usuario .btn-text").text("Actualizar");
		$("#modal-usuario").modal("show");
		/*var id_emple = this.getAttribute("rl");
		var request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
		var ajaxUrl = "/buscar_emple/"+id_emple;
		request.open("GET",ajaxUrl,true);
		request.send();
		request.onload = function(){
			if(request.status == 200){
				var objData = JSON.parse(request.responseText);
				$("#id_emple").val(id_emple);
				$("#nom_emple").val(objData[1]);
				$("#ape_emple").val(objData[2]);
				$("#dni_emple").val(objData[3]);
				$("#fech_emple").val(objData[4]);
				$("#mail_emple").val(objData[6]);
				$("#telef_emple").val(objData[7]);
				$("#distr_emple").val(objData[8]);
				$("#estado").val(objData[9]);
			}
		}*/
	});
}

function eli_usuario(){
	$("#tab_usuarios").on("click",".btn-eli-usu",function(){
		var id_usu = this.getAttribute("rl");
		Swal.fire({
			title: "Eliminar Usuario",
			text: "¿Desea eliminar este usuario?",
			icon: "question",
			showCancelButton: true,
			confirmButtonText: "Si, eliminar!",
			cancelButtonText: "No, cancelar!"
		}).then((result)=>{
			if(result.isConfirmed){
				/*var request = (window.XMLHttpRequest) ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
				var ajaxUrl = "/elim_usuario/"+id_usu;
				request.open("POST",ajaxUrl,true);
				request.send();
				request.onload = function(){
					if(request.status == 200){
						var objData = JSON.parse(request.responseText);
						Swal.fire("¡Eliminado!",objData.msj,"success");
						$("#tab_usuarios").DataTable().ajax.reload();
					}else{
						Swal.fire("Usuarios","El registro no pudo ser eliminado","error");
					}
				}*/
			}else{
				Swal.fire("Cancelado","Tu registro está seguro :)","error");
			}
		});
	});
}

function open_modal(){
	$("#modal-usuario .btn-form").removeClass("btn-primary").addClass("btn-success");
	$("#modal-usuario .modal-title").text("Registrar Usuario")
	$("#modal-usuario .btn-text").text("Registrar");
	$("#modal-usuario").modal("show");
	$("#id_usu").val("0");
	$("#form-usuario")[0].reset();
}