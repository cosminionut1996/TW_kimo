/* Slider stuff */
toggle = function() {
    if($('#licenta').is(":checked")) {
        return 'PAID';
    }
    else {
        return 'FREE';
    }
};

$('input[name=sw_licenta]').click(function(){
    $("#lb_licenta").html(toggle());
});

$('label[name=lb_licenta]').click(function(){
    $("#lb_licenta").html(toggle());
});
