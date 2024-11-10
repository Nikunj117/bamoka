/*scrolling banner*/
(function ($) {
  'use strict';

  $(document).ready(function () {
    $("#rpSlider").owlCarousel({
      autoplay: true,
      autoplayTimeout: 2000,
      autoplayHoverPause: true,
      items: 3,
      nav: true,
      loop: true,
      mouseDrag: true,
      responsiveClass: true,
      responsive: {
        0: {
          items: 1,
        },
        575: {
          items: 2,
        },
        767: {
          items: 2,
        },
        992: {
          items: 4,
        },
        1200: {
          items: 4,
        },
      },
    });
  });
})(jQuery);
