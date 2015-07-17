
$(document).ready(function(){
    /* hightlight appropriate menu items for layout page */
	$("#artistMenuItem").addClass("menuItemSelected");
	$("#artistMenuItem").addClass("artSettings");
	$("#artistMenuItem img").css("display","inline");
	$("#circleArt").css("background-color","#576F94");


	var height = $(window).height();
	var width = $(window).width();
	$(".imgTint").css('width',width+30);

	/*open picture with tint*/
	$(".imgBlock").click(function(e){
		var pictureId = $(this).attr("id");
		var tint = "tinted_";
		var newPictureId = tint.concat(pictureId);	/*id of div with tint*/
		$('#sideSelector').css('z-index','-1');
	    $("#"+newPictureId).css('display','block');


        /* set margins of image tint*/
        var margintop = $("#"+newPictureId + " img").height()/2;
        var marginleft = $("#"+newPictureId + " img").width()/2;
        $("#"+newPictureId + " img").css('margin-top', -margintop);
        $("#"+newPictureId + " img").css('margin-left', -marginleft);
	});

	/*remove picture with tint*/
	$(".imgTint").click(function(e){
		var pictureId = $(this).attr("id");
		$("#"+pictureId).css("display","none");
	});


    var  subpage = $('#subpage').val().trim();

     // highlight menu item that is selected
    if(subpage == "Layouts")
    {
        	$("#layouts").toggleClass("headerElementSelected");
    }
    else if(subpage == "Graphics")
    {
        	$("#graphics").toggleClass("headerElementSelected");
    }
     else if(subpage == "Drawings")
    {
            $("#drawings").toggleClass("headerElementSelected");
    }
    else if(subpage == "Logos")
    {
        	$("#logos").toggleClass("headerElementSelected");
    }

});


/* very last function called after document loads*/
/* set margins of images in order to center them*/
/* cannot set margin to percents because mobile devices will not render content correctly*/
/*
(function($) {
    $(window).bind("load", function() {
        $('#centerContainer img').each(function(){
            var margintop = $(this).height()/2;
            var marginleft = $(this).width()/2;
             $(this).css('margin-top',-margintop);
             $(this).css('margin-left',-marginleft);

        });
    });
})(jQuery);
*/
