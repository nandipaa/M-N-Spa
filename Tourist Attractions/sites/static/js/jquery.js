$(document).ready(function() {

      setTimeout(function() {
  location.reload();
}, 300000);

$('.carousel.carousel-multi-item.v-2 .carousel-item').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));

  for (var i=0;i<3;i++) {
    next=next.next();
    if (!next.length) {
      next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
  }
});

$(document).ready( function() {
    $('').click( function() {
        var page = $(this).attr('http://127.0.0.1:8001/sites/limpopo').split(/\?/)[1];
        $.ajax({
            type: 'POST',
            url: '/path-to-service',
            data: page,
            success: function(content) {
               $('#knp').html(content);  // replace
            }
        });
        return false; // to stop link
    });
});




});