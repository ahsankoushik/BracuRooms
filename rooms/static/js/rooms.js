


$('form').submit(function(e){
    e.preventDefault();
    let formdata = new FormData($(this)[0]);
    formdata.append('room_type',$('#room_type').val())
    $.ajax({
        url: '../api/rooms',
        type: 'post',
        data: formdata,
            headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value },
            cache: false,
            contentType: false,
            processData: false,
            success: function() { 
                console.log('success');
                window.location.href = "../rooms";
            },
            error: function(res) { 
                if(`{"room_number":["room with this room number already exists."]}`==res['responseText'])
                alert('A room with that room number already exists.'); }
    
    })
}
)