	var height = $(window).height();

	$(document).ready(function(){
		var menuHeight = $('#menu').height();
		var imageMarginTop = menuHeight+"px";
		
		$('body').css('overflow','hidden');
			
		$('#image').css('top',imageMarginTop);

		$("#homeMenuItem").addClass("menuItemSelected");
		$("#homeMenuItem").addClass("homeSettings");
	
		$("#circleIndex").css("background-color","#576F94");

		$("#homeMenuItem img").css("display","initial");
	});


