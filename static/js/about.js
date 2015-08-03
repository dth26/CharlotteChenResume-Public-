$(document).ready(function(){

    /* highlight menu items corresponding to about page */
	$("#aboutMenuItem").addClass("menuItemSelected");
	$("#aboutMenuItem").addClass("aboutSettings");
	$("#aboutMenuItem img").css("display","inline");
	$("#circleAbout").css("background-color","rgba(57,56,77,.7)");




	/*open picture with tint*/
	$(".imgOverlay").click(function(e){
		var pictureId = $(this).attr("id");

		var tint = "tinted_";
		var newPictureId = tint.concat(pictureId);	/*id of div with tint*/
	//	var scroll = $(window).scrollTop();			/*find scroll of page*/
		$("#"+newPictureId).css("display","block");
		$("body").css("overflow-y","hidden");


        var leftmargin = $("#"+newPictureId + " img").width()/2;
        var topmargin = $("#"+newPictureId + " img").height()/2;
	    $("#"+newPictureId + " img").css("margin-left",-leftmargin);
	    $("#"+newPictureId + " img").css("margin-top",-topmargin);
	});

	/*remove picture with tint*/
	$(".imgTint").click(function(e){
		var pictureId = $(this).attr("id");
		$("#"+pictureId).css("display","none");
		$("body").css("overflow-y","scroll");
	});


});
