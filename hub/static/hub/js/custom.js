(function ($) {
	
	"use strict";
//Setting the Carousel display on user page


	$('.slider-features').owlCarousel({
		items:4,
		loop:true,
		dots: false,
		nav: true,
		autoplay: true,
		margin:20,
		responsive:{
			  0:{
				  items:1
			  },
			  800:{
				  items:2
			  },
			  1000:{
				  items:3
			  },
			  1800:{
				items:4
			}
		}
	})

	

	
})(window.jQuery);
