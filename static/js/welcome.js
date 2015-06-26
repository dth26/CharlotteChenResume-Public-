$(document).ready(function(){
    $('#next').click(function(){
        var currentCenter = $('#currentCenter').attr('value');


        if(currentCenter == "one"){
            $('#one').fadeOut(1000, function(){
                $('#two').fadeIn(1500);
            });

            $('#currentCenter').attr('value','two');
        }else if(currentCenter == "two"){
            $('#two').fadeOut(1000, function(){
                $('#three').fadeIn(1500);
            });
            $('#currentCenter').attr('value','three');
        }else if(currentCenter == "three"){
           $('#three').fadeOut(1000, function(){
                $('#three').css('display','none');
                $('#four').fadeIn(1500);
            });
            $('#currentCenter').attr('value','four');
        }
        else if(currentCenter == "four"){
            var url = "http://pythonprogrammer.pythonanywhere.com/";
 		    window.open(url, '_self' );
        }
    });
});