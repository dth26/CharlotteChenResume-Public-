

var width = $(window).width();
var height = $(window).height();
/* check if device supports touch */
var supportsTouch = 'ontouchstart' in window || navigator.msMaxTouchPoints;

$(document).ready(function(){


    /* set left of centerContainer*/
    var left = width/2 + 'px';
    $('#centerContainer').css('left',left);

    /* if user click login key submit form to userLog.py script */
	$('#submitLogin').click(function(){
		var marginleft = $('#loginItem').css('margin-left');

        /* only open up item onclick if sideselector item is fully expanded. for mobile platforms */
        if(marginleft == '-240px')
        {
        	$('#loginForm').submit();
        }
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



    /* implemented for devices that do not use touch and can sense hover */
    // if(!supportsTouch){
    //     /* show sideSelector menuItem if hovered over */
    // 	$('.slideItem').mouseenter(function(){
    // 	    $('#menuRight').css('overflow','visible');
    // 	    $(this).addClass('boxShadow');
    // 	    $(this).css('z-index','1002'); // make shadow of current slideItem overshadow that other slideItems
    // 		$(this).stop(true,true).animate({"margin-left": '-=240'});
    // 	}).mouseleave(function(){
    // 	    $(this).stop(true,true).animate({"margin-left": '+=240'}, function(){
    // 	        // when animation is done exectue this
    // 	        $('#menuRight').css('overflow','hidden');
    // 	        $(this).removeClass('boxShadow');
    // 	    });
    // 	});
    // }


    if(true){

        var animated = 0;
    	$('.slideItem').click(function(){

    	    if(animated == 1 ){
                return;
            }else{
                animated = 1;
            }

    	    var marginleft = $(this).css('margin-left');
    	    var slideItemId = '#' + $(this).attr('id');

    	    if(marginleft == '-240px'){
                closeRightMenuItem(slideItemId);
    	    }else if(marginleft == '0px'){
    	        $('.slideItem').each(function(){
    	             var currID = '#' + $(this).attr('id');
    	             var currMargin = $(this).css('margin-left');
    	             if(currMargin != '0px' ){
    	                 closeRightMenuItem(currID);
    	             }
    	        });
    	        setTimeout(function(){
    	            openRightMenuItem(slideItemId);
    	        },500);
    	    }
    	});

    }
    /* expands right menu item to left */
    function openRightMenuItem(id){
         $('#menuRight').css('overflow','visible');
    	 $(id).addClass('boxShadow');
    	 $(id).stop(true,true).animate({"margin-left": '-=240'}, function(){
    	     animated = 0;
    	 });
    }
    /* unexpands right menu item to right */
    function closeRightMenuItem(id){
        $(id).stop(true,true).animate({"margin-left": '+=240'},function(){
            $('#menuRight').css('overflow','hidden');
            $(id).removeClass('boxShadow');
            animated = 0;
        });
    }

    /* open url when sideselector menu item is clicked */
    $('.rightMenuItemImg').click(function(){
        var itemID = $(this).attr('id');

        var items = {
            'linkedItemImg'   : "https://www.linkedin.com/profile/view?id=289654202&authType=NAME_SEARCH&authToken=IZBw&locale=en_US&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2Cidx%3A1-1-1%2CtarId%3A1434727653030%2Ctas%3Achar",
            'resumeItemImg'   : "../static/files/resume.pdf",
            'questionItemImg' : "http://www.meetcharlottechen.com/build"
        };

        var url = items[itemID];
        // get id of parent div menu item
        var divItem = '#' + itemID.substring(0, itemID.length-3);
        var marginleft = $(divItem).css('margin-left');

        /* only open up item onclick if sideselector item is fully expanded. for mobile platforms */
        if(marginleft == '-240px')
        {
        	window.open(url, '_blank');
        }
    });


    /*
        if device supports touch that means the device is probably a phone.
        if user zooms in hide right menu bar
    */
    if(supportsTouch && supportsTouch != undefined)
    {
        window.setInterval(function(){
           onZoom();
        }, 3);
    }
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
        $('#menuRight').fadeOut(1000);
	}else{
	    $('#menuRight').css('display','block');
	}
}





