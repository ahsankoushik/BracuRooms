room = window.localStorage.getItem('room')
if ( room!== 'false'){
    $.notify({title :'New Room Added', content:'New Room Added '+room, timeout:5000});

    window.localStorage.setItem('room','false')
}



$('form').submit(function(e){
    e.preventDefault();
    let formdata = new FormData($(this)[0]);
    let room_type = $('#room_type').val()
    formdata.append('room_type',room_type)
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
                window.localStorage.setItem('room',$('#room_number').val() + '(' + room_type +')')
                window.location.href = "../rooms"
            },
            error: function(res) { 
                if(`{"room_number":["room with this room number already exists."]}`==res['responseText'])
                alert('A room with that room number already exists.'); }
    
    })
}
)