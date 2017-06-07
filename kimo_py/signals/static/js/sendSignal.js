

//$('#mySelect').change(function(){
//    var value = $(this).val();
//});

function populateId(id){

$('#name').attr('value', id)
    if($('#description').val()){
        $('#submitbtn').css('visibility','visible');

    }


}

function populateMessage(message){

$('#description').attr('value', message);
    if($('#name').val()){
        $('#submitbtn').css('visibility','visible');
}
}