function menu_active() {

    var url = document.location.pathname;

    $("#side-menu a").each(function () {
        var href = $(this).attr('href');
        if (url == href){
            $(this).addClass('active');

        }else if(url == "/cmdb/"){
            if(href == "/cmdb/index.html"){
                $(this).addClass('active');
            }
        }


    })

}
menu_active();




$(function () {

    $("#side-menu a").click(function () {

        $("#side-menu a").removeClass('active');

        var next_tag = $(this).next();
        var ul_num = next_tag.length;

        if(ul_num > 0){   // 有下一级

            var status = $(this).parent('li').hasClass('active');

            if(status){
                $(this).parent('li').removeClass('active');
                next_tag.removeClass('in')
            }else{
                $(this).parent('li').addClass('active');
                next_tag.addClass('in')
            }

        }else{

        }
    })

});




