(function ($) {
 "use strict";
$(document).ready(function(){
	  
		/*
		Mean Menu Responsive
		============================*/		
        jQuery('nav#main-menu').meanmenu();						
		/*
		Testimonial Crousel
		============================*/ 
		
		  $(".all-testimonial").owlCarousel({
			autoPlay: false, 
			slideSpeed:2000,
			pagination:false,
			navigation:true, 
			items :1,
			navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
			itemsDesktop : [1199,1],
			itemsDesktopSmall : [980,1],
			itemsTablet: [768,1],
			itemsTablet: [767,1],
			itemsMobile : [479,1],
		  });
		  
		/*
		Patner Crousel
		============================*/ 
		  $(".all-patner").owlCarousel({
			autoPlay: false, 
			slideSpeed:2000,
			pagination:false,
			navigation:true, 
			items : 6,
			navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
			itemsDesktop : [1199,6],
			itemsDesktopSmall : [980,5],
			itemsTablet: [768,5],
			itemsMobile : [479,3],
		  });			
		
		/*
		Slider Crousel
		============================*/ 
		  $(".all-slide").owlCarousel({
			autoPlay: false, 
			slideSpeed:1500,
			pagination:false,
			navigation:true, 
			mouseDrag: false,
			items :1,
			navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
			itemsDesktop : [1199,1],
			itemsDesktopSmall : [980,1],
			itemsTablet: [768,1],
			itemsMobile : [479,1],
		  });
	  
		  
		/*
		scrollUp
		============================*/	
		$.scrollUp({
			scrollText: '<i class="fa fa-angle-up"></i>',
			easingType: 'linear',
			scrollSpeed: 900,
			animation: 'fade'
		});	
		/*
		Counter Js
		============================*/ 
        $('.counter').counterUp({
            delay: 10,
            time: 1000			
        }); 				
		 /*
		Related Chef Crousel
		============================*/ 
		  $(".all-related-chef").owlCarousel({
			autoPlay: false, 
			slideSpeed:2000,
			pagination:false,
			navigation:true, 
			items : 3,
			navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
			  itemsDesktop : [1199,3],
			itemsDesktopSmall : [980,3],
			itemsTablet: [768,2],
			itemsMobile : [479,1],
		  });
  
		/*
		Preeloader
		============================*/
		$(window).load(function() {
			$('#preloader').fadeOut();
			$('#preloader-status').delay(200).fadeOut('slow');
			$('body').delay(200).css({'overflow-x':'hidden'});
		});
		
	});	
})(jQuery);

