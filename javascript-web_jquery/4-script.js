#!/usr/bin/node
$("#toggle_header").click(function() {
    var header = $("header");
    if (header.hasClass("red")) {
      header.removeClass("red");
      header.addClass("green");
    } else {
      header.removeClass("green");
      header.addClass("red");
    }
  });