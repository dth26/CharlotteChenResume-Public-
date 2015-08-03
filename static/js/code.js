$(document).ready(function(){
    /* highlight appropriate menu items corresponding to developer page */
	$("#developerMenuItem").addClass("menuItemSelected");
	$("#developerMenuItem").addClass("developerSettings");
	$("#developerMenuItem img").css("display","inline");
    $("#circleCode").css("background-color","rgba(57,56,77,.7)");


	$("#cssmenu > ul > li > a").click(function(){
		$(this).css("background-color","#B4B8D4");
	});


});
