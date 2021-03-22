  $( document ).ready(function() {

 var $header = $('header');
 var $sticky = $header.before($header.clone().addClass("sticky"));

   $(window).on("scroll", function(){
 var scrollFromTop  = $(window).scrollTop();
 $("body").toggleClass("scroll", (scrollFromTop > 350 ));

 });


  var body = $('body');
    var menuTrigger = $('.js-menu-trigger');
    var mainOverlay = $('.js-main-overlay');

    menuTrigger.on('click', function(){
       body.addClass('menu-is-active');

    });


});