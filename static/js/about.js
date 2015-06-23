$(document).ready(function(){
	$("#aboutMenuItem").addClass("menuItemSelected");
	$("#aboutMenuItem").addClass("aboutSettings");
	$("#aboutMenuItem img").css("display","initial");
	$("#circleAbout").css("background-color","#576F94");

    $('.smallImg').hover(function() {
	     $(this).css("visibility","hidden");
	     var spanID = $(this).attr("id");
	     $("#"+spanID+"Span").css("display", "block");

	},function() {
		   sleep(500);
		  $(this).css("visibility","visible");
		  var spanID = $(this).attr("id");
		  $("#"+spanID+"Span").css("display", "none");
	});


  var height = $(window).height();
    $(".imgTint").css('height',height);
	$(".imgTint").css('width',width+30);

	/*open picture with tint*/
	$(".imgOverlay").click(function(e){
		var pictureId = $(this).attr("id");
		var tint = "tinted_";
		var newPictureId = tint.concat(pictureId);	/*id of div with tint*/
		var scroll = $(window).scrollTop();			/*find scroll of page*/
		$("#"+newPictureId).css("display","block");
		$("body").css("overflow-y","hidden");
	});

	/*remove picture with tint*/
	$(".imgTint").click(function(e){
		var pictureId = $(this).attr("id");
		$("#"+pictureId).css("display","none");
		$("body").css("overflow-y","scroll");
	});


});
