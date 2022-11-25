// $('select').selectize()
var t;
$.ajax({
    url : '../api/rooms',
    type : 'get',
    dataType : 'json',
    success : function(res){
        t = res;
        let option;
        for(x in res){
            option = document.createElement("option");
            option.text = res[x]['room_number'] + '(' + res[x]['room_type'] +')';
            option.value = res[x]['id'];
            // if(sel != undefined && x==sel){
            //     option.selected = true;
            // }
            document.getElementById("room").appendChild(option);
        }
        $('select').selectize()

    },
    error : function(e){
        console.log(res);
    }
})


var count = 2;

function add_another(){
    if(count >3){
        alert("You can't select more than 3.");
        return
    }
    let html = `
    <div class="col col-12">
        <div class="mb-3">
            <label class="form-label" for="room">Time:</label>
            <select id="time_${count}" placeholder="room_number">
                <option value="1">8:00am - 9:20am</option>
                <option value="2">9:30am - 10:50am</option>
                <option value="3">11:00am - 12:20am</option>
                <option value="4">12:30am - 1:50am</option>
                <option value="5">2:00am - 3:20am</option>
                <option value="6">3:30am - 5:20am</option>
              </select>
        </div>
    </div>`;
        let div = document.createElement("div");
        div.classList.add("row");
        div.id=`row_${count}`;
        div.innerHTML = html;
        document.getElementById("times").appendChild(div);
        // let clone = product_select.cloneNode(true);
        // clone.setAttribute('id','id_product_'+(count));
        // document.getElementById("id_product_"+count).replaceWith(clone);
        $('#time_'+count).selectize({
            sortField: 'data-value',
        });
        count += 1;
}

function remove_last(){
    if(count>2){
        document.getElementById(`row_${count-1}`).remove();
        count -= 1;
    }
}



$('form').submit(function(e){
    e.preventDefault();
    let formdata = new FormData($(this)[0]);

    // Display the key/value pairs

    let times = "";
    for(x=1;x<count;x++){
        times += $(`#time_${x}`).val() +',';
    }
    formdata.append('room',$('#room').val());
    formdata.append('time_slot',times);
    formdata.append('reason',$('#reason').val())




    // for (var pair of formdata.entries()) {
    //     console.log(pair[0]+ ', ' + pair[1]); 
    // }
    
    
    $.ajax({
        url: '../api/bookings',
        type: 'post',
        data: formdata,
            headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value },
            cache: false,
            contentType: false,
            processData: false,
            success: function() { 
                console.log('succes');
                window.location.href = "../apply";
            },
            error: function(res) { console.log(res); }
    
    })
}
)