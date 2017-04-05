/**
 * Created by cody on 4/3/2017.
 */

$(document).ready(function () {

    /* Side menu  --- START  ----- */
    if( localStorage.getItem("sidemenu_flag") == 'open' ) {
        $('.side-menu').css('display', 'block');
        $('.content-main').css('margin-left', '260px');
    } else {
        $('.side-menu').css('display', 'none');
        $('.content-main').css('margin-left', '0px');
    }

    $('#button-sidemenu').bind('click', function () {
        $('.side-menu').animate({
            height: 'toggle',
        });
        if ( localStorage.getItem("sidemenu_flag") == 'open' ) {
            localStorage.setItem("sidemenu_flag", 'close');
            $('.content-main').animate({
                marginLeft: '0px',
            });
        }else {
            localStorage.setItem("sidemenu_flag", 'open');
            $('.content-main').animate({
                marginLeft: '260px',
            });
        }
    });

    $('.title').bind('click', function(){
        var result = $(this).attr('id');
        // alert(result);
    });

    if ( localStorage.getItem("entry-selected")  ) {
        var item_id = localStorage.getItem("entry-selected");
        $("#" + item_id).addClass("entry-selected");
        $("#" + item_id).removeData("entry");
    }

    $('.entry').bind('click', function() {
        var entry = $(this).attr('id');
        localStorage.setItem("entry-selected", entry);

        $('.entry').attr('class', 'entry');

        $(this).addClass("entry-selected");
        $(this).removeData("entry");
    });

    /* Side menu  --- END  ----- */

});