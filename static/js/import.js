$(document).ready(function(){
    var path = window.location.pathname;
    if (path == "/line"){
        $(document.getElementsByClassName("aside-item")[0]).addClass("selected");
        $('.content').load("/line");
    }else if(path == "/whatsapp"){
        $(document.getElementsByClassName("aside-item")[1]).addClass("selected");
        $('.content').load("/whatsapp");
    }
    $('a').on('click', function(event) {  
        $(this).addClass('selected'); })
})

