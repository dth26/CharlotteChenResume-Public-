	var height = $(window).height();

$(document).ready(function(){
	var menuHeight = $('#menu').height();
	$('body').css('overflow','hidden');

    /* highlight appropriate menu items for index page */
	$("#homeMenuItem").addClass("menuItemSelected");
	$("#homeMenuItem").addClass("homeSettings");
	$("#circleIndex").css("background-color","#576F94");
	$("#homeMenuItem img").css("display","inline");

    /* remove extra overflow on mobile platforms*/
	$('#force').css('overflow','hidden');
});


/* set position of image on index page, ensures image does not overlap menu */
function setImageHeight(){
        var menuHeight = $('#menu').height();
    	var docHeight = $(document).height() ;
    	var imageMarginTop = menuHeight+"px";
		$('#image').css('top',imageMarginTop);
        $('#image').css('height',docHeight + 'px');
}


/* very last function called after document loads*/
(function($) {
    $(window).bind("load", function() {
        setImageHeight();
    });
})(jQuery);

/* change height of picture if orientation changes */
window.onorientationchange = function(){
    setImageHeight();
};