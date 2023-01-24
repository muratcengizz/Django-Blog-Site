var createDots = function() {
  var nav = $('#slider-nav ul');
  var slides = $('.slide').length;
  for(var i = 0; i < slides; i++) {
    nav.append('<li class="dot">&bull;</li>');
  }
  $('.dot').first().addClass("active-dot");
};

// Next slide transition
var next = function() {
	var activeSlide = $('.active-slide');
	var nextSlide = activeSlide.next('.slide');
	if(nextSlide.length == 0) {
		nextSlide = $('.slide').first();
	}	activeSlide.fadeOut('slow').removeClass("active-slide");
	nextSlide.fadeIn(1000).addClass("active-slide");
	
	var activeDot = $('.active-dot');
	var nextDot = activeDot.next('.dot');
	if(nextDot.length == 0) {
		nextDot = $('.dot').first();
	}
	activeDot.removeClass("active-dot");
	nextDot.addClass("active-dot");	
};
var prev = function() {
  var activeSlide = $('.active-slide');
  var prevSlide = activeSlide.prev('.slide');
  if(prevSlide.length == 0) {
    prevSlide = $('.slide').last();
  }
   activeSlide.fadeOut('slow').removeClass("active-slide");
   prevSlide.fadeIn(1000).addClass("active-slide");
  
   var activeDot = $('.active-dot');
	var prevDot = activeDot.prev('.dot');
	if(prevDot.length == 0) {
		prevDot = $('.dot').last();
	}
	activeDot.removeClass("active-dot");
	prevDot.addClass("active-dot");	
};
var clickDot = function(dot) {
  var activeSlide = $('.active-slide');
		var i = $(dot).index() + 1;
     var nextSlide = $('.slide:nth-child('+i+')');
     activeSlide.fadeOut('slow').removeClass("active-slide");
     nextSlide.fadeIn(1000).addClass("active-slide");
     $('.active-dot').removeClass("active-dot");
     $(dot).addClass("active-dot");
};
var createSlide = function(url) {
  if($('.slide').length < 10) {
     // Create the slide
		var slide = $('<div class="slide"></div>');
		var img = $('<img src="' + url + '" class="slide-img" />');
		slide.append(img);
		$('#slides').append(slide);
		// Create the dot
		var nav = $('#slider-nav ul');
		var dot = '<li class="dot">&bull;</li>';
		nav.append(dot);
		$('.dot').last().click(function() {
			clickDot(this);
		});
  }
};
var editSlide = function(url) {
  var img = $('.active-slide .slide-img');
  img.attr("src", url);
};
var deleteSlide = function() {
  if($('.slide').length > 2) {
    var activeSlide = $('.active-slide');
    var prevSlide = activeSlide.prev('.slide');
    activeSlide.remove();
	 if(prevSlide.length == 0) {
		prevSlide = $('.slide').first();
	 }
		prevSlide.fadeIn('slow').addClass("active-slide");

	 var activeDot = $('.active-dot');
	 var prevDot = activeDot.prev('.dot');
	 activeDot.remove();
	 if(prevDot.length == 0) {
		prevDot = $('.dot').first();
	 }
	 prevDot.addClass("active-dot");
  }
};
var slideLoop;
var showDialog = function(show) {
  if(show) {
    $('#dialog').fadeIn('slow');
    clearInterval(slideLoop);
  } else {
    $('#dialog').fadeOut('slow');
  }
  return show;
};
var main = function() {
  var mili = 5000;
  var dialog = false;
  createDots();
  
  // Move automaticaly through the slides
  slideLoop = setInterval(next,mili);
  $('#slider').mouseenter(function() {
    $('.arrow').fadeIn('slow');
    $('#update-btn').fadeIn('slow');
    if(!dialog) {
      clearInterval(slideLoop);
    }
  });
  $('#slider').mouseleave(function() {
    $('.arrow').fadeOut('slow');
    $('#update-btn').fadeOut('slow');
    if(!dialog) {
      slideLoop = setInterval(next,mili);
    }
  });
  $('.right').click(next);
  $('.left').click(prev);
  // Clicking a dot move to the corresponding slide
  $('.dot').click(function() {
		clickDot(this);
  });
  // Update slide buttons
  $('#add').click(function() {
      $('#ok').unbind();
      $('#input').val("");
      $('#ok').click(function() {
        var url = $('#input').val();
        createSlide(url);
        dialog = showDialog(false);
      });
      $('#msg').html("Add slide");
      $('#ok').html("Add");
      $('#input').css("display", "block");
      dialog = showDialog(true);
  });
  $('#edit').click(function() {
    $('#ok').unbind();
    $('#input').val("");
    $('#ok').click(function() {
      var url = $('#input').val();
      editSlide(url);
      dialog = showDialog(false);
    });
    $('#msg').html("Edit Slide");
    $('#ok').html("Update");
    $('#input').css("display", "block");
    dialog = showDialog(true);
  });
  $('#remove').click(function() {
    $('#ok').unbind();
    //$('#input').val("");
    $('#ok').click(function() {
      deleteSlide();
      dialog = showDialog(false);
    });
    $('#msg').html("Remove Slide?");
    $('#ok').html("Remove");
    $('#input').css("display", "none");
    dialog = showDialog(true);
  });
  $('#cancel').click(function() {
      dialog = showDialog(false);
  });
};

$(document).ready(main);