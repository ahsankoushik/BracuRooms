$('form').submit(function(e){
    e.preventDefault();
    let formdata = new FormData($(this)[0]);
    formdata.append('time_slot',$('#time_1').val())
    $.ajax({
        url: '../api/free_room_st',
        type: 'post',
        data: formdata,
            headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value },
            cache: false,
            contentType: false,
            processData: false,
            success: function(res) { 
                // console.log(res);
                let html = '';
                for(x in res){
                    room =res[x].__str__.split('(')
                    // console.log(res[x].faculty);
                    html += `<tr class="text-center" id ="${res[x].id}">
                        <td>${room[0]}</td>
                        <td>${room[1].slice(0,-1)}</td>
                        <td><button class="btn btn-primary" onclick="book_a_seat(${res[x].id})">Book</button></td>
                    </tr>`;
                }
                document.getElementById('room_details').innerHTML = html;
                
                
            },
            error: function(res) { 
                // if(`{"room_number":["room with this room number already exists."]}`==res['responseText'])
                // alert('A room with that room number already exists.'); 
                console.log('error');
                console.log(res);
            }
    
    })
}
)

function book_a_seat(room){
    $.ajax({
        url:`../api/book_a_seat/${room}`,
        type:'GET',
        
        success:(function(res){
            // window.location.href = '../apply';
            // console.log(res.status);


            $.notify({title :'Success', content:'A seat has booked ', timeout:5000});

            
        }),
        error: (function(e){
            console.log('error');
            if (e.status == 409){
                alert("You have a privous booking")
            }
        })

    })

}