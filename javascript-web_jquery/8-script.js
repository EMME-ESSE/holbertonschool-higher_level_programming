#!/usr/bin/node
$(document).ready(function(){
    $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(result){
        $.each(result.results, function(index, movie){
            $("#list_movies").append("<li>" + movie.title + "</li>");
        });
    });
});
