$(document).ready(function(){
	$(".cuenta-h").addClass("menu-open");
	$(".cuenta").addClass("active");
	$(".perfil").addClass("active");
	$(".s-cuenta").css("display","block");
	pestañas();
});

function pestañas(){
	var triggerTabList = [].slice.call(document.querySelectorAll('#opc-usu a'))
	triggerTabList.forEach(function (triggerEl) {
	  	var tabTrigger = new bootstrap.Tab(triggerEl)

	  	triggerEl.addEventListener('click', function (event) {
	    	event.preventDefault()
	    	tabTrigger.show()
	  	})
	});
}