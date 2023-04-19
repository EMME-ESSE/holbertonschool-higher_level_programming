#!/usr/bin/node
$(document).ready(function(){
    $.ajax({
        url: "https://stefanbohacek.com/hellosalut/?lang=fr",
        success: function(result){
            $("#hello").text(result.hello);
        }
    });
});
