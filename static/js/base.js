

var width = $(window).width();
var height = $(window).height();

$(document).ready(function(){

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



	$('.slideItem').mouseenter(function(){
		$(this).stop(true,true).animate({"margin-left": '-=220'});
	}).mouseleave(function(){
		$(this).stop(true,true).animate({"margin-left": '+=220'});
	});


	$('#linkedItem').click(function(){
 		var url = "https://www.linkedin.com/profile/view?id=289654202&authType=NAME_SEARCH&authToken=IZBw&locale=en_US&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2Cidx%3A1-1-1%2CtarId%3A1434727653030%2Ctas%3Achar";
 		window.open(url, '_blank');

	});

	$('#resumeItem').click(function(){
 		var url = "../static/files/resume.pdf";
 		window.open(url, '_blank');
	})
/*
	var docHeight = $(document).height();
	var docWidth = $(document).width();
	docHeight = docHeight + "px";
	docWidth = docWidth + "px";
	//$('#force').css('height',docHeight);
  //  var menuWidth = $('#force').width() + "px";
   // $('#menu').css('width',menuWidth);
   */
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


function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function addStar(parent){

	var elem = document.createElement("img");
	elem.setAttribute("src", "");
	document.getElementById(parent).appendChild(elem);

}