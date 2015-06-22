$(document).ready(function(){
	$("#developerMenuItem").addClass("menuItemSelected");
	$("#developerMenuItem").addClass("developerSettings");
	$("#developerMenuItem img").css("display","initial");

//	addStar('developerMenuItem');

	$("#cssmenu > ul > li > a").click(function(){
		$(this).css("background-color","#B4B8D4");
	});

	$("#circleCode").css("background-color","#576F94");

});
