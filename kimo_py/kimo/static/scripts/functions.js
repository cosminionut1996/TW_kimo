/* Toggle all checkboxes stuff */
function toggle(source, name) {
    checkboxes = document.getElementsByName(name);
    for(var i=0, n=checkboxes.length;i<n;i++) {
        checkboxes[i].checked = source.checked;
    }
}

/* Resize container fluid in KIMO
$("body > #top").css('height', $(window).height() * 90 / 100);
*/

/* Spinner-related stuff */
function show_loader() {
    document.getElementById("loader").style.visibility = 'visible';
}
function hide_loader() {
    document.getElementById("loader").style.visibility = 'hidden';
}
$("a").click(show_loader)
$(window).bind("load", hide_loader)
$(document).bind("load", hide_loader)



/* Dragbar sizing stuff */
var down;
$("#top").css('height', $(window).height() - $("#footer").height() - 40);
$("#dragbar").mousedown(function(e){ down = true;});
$("#dragbar").mouseup(function(e) {
  down = false;
  $("#top").css('height', e.pageY - 20);
  $("#footer").css('height', $(window).height() - e.pageY);
  $("#error").css('height', $(window).height() - e.pageY - 20);
});
$("*").mousemove(function(e) {
  if(down)
    $("#footer").css('height', $(window).height() - e.pageY);
});
$("*").mouseup(function(e) {
  	down = false;
});


/* Home login form stuff... */
$(function() {
    $('#login-form-link').click(function(e) {
    	$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});

$("#myonoffswitch").mousedown(function(e) {
    $("#p1").css("opacity", 0.4);
})

$("#myonoffswitch1").mousedown(function(e) {
    $("#p2").css("opacity", 0.4);
})