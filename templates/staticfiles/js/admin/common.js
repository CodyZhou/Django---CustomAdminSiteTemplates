/**
 * Created by cody on 4/3/2017.
 */

$(document).ready(function () {

    /* Side menu  --- START  ----- */
    if( localStorage.getItem("side-menu-flag") == 'open' ) {
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
        if ( localStorage.getItem("side-menu-flag") == 'open' ) {
            localStorage.setItem("side-menu-flag", 'close');
            $('.content-main').animate({
                marginLeft: '0px',
            });
        }else {
            localStorage.setItem("side-menu-flag", 'open');
            $('.content-main').animate({
                marginLeft: '260px',
            });
        }
    });

    if ( localStorage.getItem("open-title") ) {
        var open_titles = JSON.parse(localStorage.getItem("open-title"));
        $.each(open_titles, function(key, value){
            // alert(value);
            $('#collapse-' + value).addClass('in');
            $('#'+value+' span').addClass('glyphicon-chevron-down');
            $('#'+value+' span').removeClass('glyphicon-chevron-right');
        });
    }

    $('.title').bind('click', function(){
        var result = $(this).attr('id');
        var open_titles = JSON.parse(localStorage.getItem("open-title"));

        if ( open_titles == null ) {
            open_titles = new Array();
            open_titles.push(result);
        } else {
            var flag = $.inArray(result, open_titles);
            if ( flag >= 0 ) {
                open_titles.splice(flag, 1);
                $('#' + result + ' span').addClass('glyphicon-chevron-right');
                $('#' + result + ' span').removeClass('glyphicon-chevron-down');
            } else {
                open_titles.push(result);
                $('#' + result + ' span').addClass('glyphicon-chevron-down');
                $('#' + result + ' span').removeClass('glyphicon-chevron-right');
            }
        }
        // alert(open_titles);

        localStorage.setItem("open-title", JSON.stringify(open_titles));
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