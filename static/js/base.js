

var width = $(window).width();
var height = $(window).height();

$(document).ready(function(){

    /* set left of centerContainer*/
    var left = width/2 + 'px';
    $('#centerContainer').css('left',left);

    /* if user click login key submit form to userLog.py script */
	$('#submitLogin').click(function(){
		//alert({{ url_for("login") }});
		$('#loginForm').submit();
	});



	/* opening the editPane*/
	$(".openEditPane").click(function(e){
		var id = $(this).attr('id');
		$("#menu").css("z-index","-1");	// hide menu when tinted editpane appears
		$("#"+id+"Overlay").css("display","block");
	});


	/* close a setting div*/
	/*remove picture with tint*/
	$(".closeEditPane").click(function(e){
		var id = $(this).attr('id');
		$("#"+id).css("display","none");
		$("#menu").css("z-index","3");
	});


    /* check if device supports touch */
    var supportsTouch = 'ontouchstart' in window || navigator.msMaxTouchPoints;
    /* implemented for devices that do not use touch and can sense hover */
    if(!supportsTouch){
        /* show sideSelector menuItem if hovered over */
    	$('.slideItem').mouseenter(function(){
    	    $(this).css('z-index','1002'); // make shadow of current slideItem overshadow that other slideItems
    		$(this).stop(true,true).animate({"margin-left": '-=220'});
    	}).mouseleave(function(){
    	    $(this).stop(true,true).animate({"margin-left": '+=220'});
    	});
    }

    /* implemented for tablet/mobile devices that cannot detect hover */
    if(supportsTouch && supportsTouch != undefined){

        window.setInterval(function(){
            onZoom();
        }, 3);

    	$('.slideItem').click(function(){
    	    var marginleft = $(this).css('margin-left');
             $(this).css('z-index','1002'); // make shadow of current slideItem overshadow that other slideItems
    	    if(marginleft == '-220px'){
    	        $(this).stop(true,true).animate({"margin-left": '+=220'});
    	    }else if(marginleft == '0px'){
    	        $(this).stop(true,true).animate({"margin-left": '-=220'});
    	    }
    	});
    }

    /* open url when sideselector menu item is clicked */
    $('.slideItem').click(function(){
        var itemID = $(this).attr('id');
        var items = {
            'linkedItem'   : "https://www.linkedin.com/profile/view?id=289654202&authType=NAME_SEARCH&authToken=IZBw&locale=en_US&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2Cidx%3A1-1-1%2CtarId%3A1434727653030%2Ctas%3Achar",
            'resumeItem'   : "../static/files/resume.pdf",
            'questionItem' : "http://www.meetcharlottechen.com/build"
        };

        var url = items[itemID];
        var marginleft = $(this).css('margin-left');
        /* only open up item onclick if sideselector item is fully expanded. for mobile platforms */
        if(marginleft == '-220px')
        {
        	window.open(url, '_blank');
        }
    });


});



/* very last function called after document loads*/
(function($) {
    $(window).bind("load", function() {
        var docHeight = $(document).height();
        var docWidth = $(document).width() + 'px';
		docHeight = docHeight + "px";
		$('#force').css('height',docHeight);

	//    $('body').hide().fadeIn(1000, function() {});
    });
})(jQuery);

/* used on about page. helps with smooth imageoverlay on hover */
function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}


/* hide sideSelector if window is minimized */
$(window).resize(function(){
    var docWidth = $(document).width();
    var windowWidth = window.outerWidth;
    if(windowWidth <  screen.availWidth - 50){
        $('#sideSelector').fadeOut(1000);
    }else{
        $('#sideSelector').hide().fadeIn(1000);
    }
});

/* mobile: if page is zoomed in hide sideSelector */
function onZoom(){

    var zoom = (document.width / window.innerWidth);
    	/* for mobile to detect zoom, if ratio greater than 1 then mobile is zoomed */
	if(zoom > 1.5){
        $('#sideSelector').fadeOut(1000);
	}else{
	    $('#sideSelector').css('display','block');
	}
}





