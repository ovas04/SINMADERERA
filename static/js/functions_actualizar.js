$(document).ready(function(){
	$(".actualizar").addClass("active");
	tipo_archivo();
	actualizar_priv();
	actualizar_pub();
});

function tipo_archivo(){
	$("#form-actualizar").on("change","#tipo",function(){
		var tipo = $("#tipo").val();
		if(tipo == 1){
			$(".archivo").css("display","block");
			$(".link").css("display","none");
		}else{
			$(".archivo").css("display","none");
			$(".link").css("display","block");
		}
	});
}

function actualizar_priv(){
	$(".btn-actualizar").click(function(){
		Swal.fire({
			title: "Actualizar construcciones",
			text: "¿Desea actualizar los registros de construcciones privadas?",
			icon: "question",
			showCancelButton: true,
			confirmButtonText: "Si, actualizar!",
			cancelButtonText: "No, cancelar!"
		}).then((result)=>{
			if(result.isConfirmed){

			}else{
				Swal.fire("Cancelado","Tus registros estás seguros :)","error");
			}
		});
	});
}

function actualizar_pub(){
	
}