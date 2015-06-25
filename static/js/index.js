	var height = $(window).height();

$(document).ready(function(){
	var menuHeight = $('#menu').height();
	$('body').css('overflow','hidden');

    /* highlight appropriate menu items for index page */
	$("#homeMenuItem").addClass("menuItemSelected");
	$("#homeMenuItem").addClass("homeSettings");
	$("#circleIndex").css("background-color","#576F94");
	$("#homeMenuItem img").css("display","inline");
});




/* very last function called after document loads*/
/* set position of image on index page, ensures image does not overlap menu */
(function($) {
    $(window).bind("load", function() {
    	var docHeight = $(document).height() + 'px';
    	var imageMarginTop = menuHeight+"px";
		$('#image').css('height',docHeight);
		$('#image').css('top',imageMarginTop);
    });
})(jQuery);
