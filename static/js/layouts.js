
$(document).ready(function(){
	$("#artistMenuItem").addClass("menuItemSelected");
	$("#artistMenuItem").addClass("artSettings");


	var height = $(window).height();
	var width = $(window).width();
	$(".imgTint").css('height',height);
	$(".imgTint").css('width',width+30);

	/*open picture with tint*/
	$(".imgBlock").click(function(e){
		var pictureId = $(this).attr("id");
		var tint = "tinted_";
		var newPictureId = tint.concat(pictureId);	/*id of div with tint*/
	//	$('#menu').css('z-index','-1');
		$('#sideSelector').css('z-index','-1');
	    $("#"+newPictureId).css('display','block');
//		$("body").css("overflow-y","hidden");
	});

	/*remove picture with tint*/
	$(".imgTint").click(function(e){
		var pictureId = $(this).attr("id");
		$("#"+pictureId).css("display","none");
	});


	$("#circleArt").css("background-color","#576F94");
});
