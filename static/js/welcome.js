$(document).ready(function(){


    var animated = 0;

    $('#next').click(function(){
        var currentCenter = $('#currentCenter').attr('value');

        if(animated === 1) return;
        animated = 1;

        if(currentCenter == "one"){
            $('#one').fadeOut(1000, function(){
                $('#two').fadeIn(1500, function(){
                    animated = 0;
                });
            });

            $('#currentCenter').attr('value','two');
        }else if(currentCenter == "two"){
            $('#two').fadeOut(1000, function(){
                $('#three').fadeIn(1500, function(){
                    animated = 0;
                });
            });
            $('#currentCenter').attr('value','three');
        }else if(currentCenter == "three"){
           $('#three').fadeOut(1000, function(){
                $('#four').fadeIn(1500, function(){
                    animated = 0;
                });
            });
            $('#currentCenter').attr('value','four');
        }
        else if(currentCenter == "four"){
             $('#four').fadeOut(1000, function(){
                $('#five').fadeIn(1500, function(){
                    animated = 0;
                });
            });
            $('#currentCenter').attr('value','five');
        }
        else if(currentCenter == "five"){
             $('#five').fadeOut(1000, function(){
                $('#six').fadeIn(1500, function(){
                    animated = 0;
                });
            });
            $('#currentCenter').attr('value','six');

            if( $('#user').val() == 0){
                $('#next').css('display','none');
            }
        }
        else if(currentCenter == "six"){
            var url = "http://www.meetcharlottechen.com";
 		    window.open(url, '_self' );
        }
    });

});
























