// $('select').selectize()
// $('#date').datepicker({
//     format:'yyyy/mm/dd',
// }).datepicker("setDate",'now');
let today = new Date();
let dd = String(today.getDate()).padStart(2, '0');
let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
let yyyy = today.getFullYear();
document.getElementById('date').value = `${yyyy}-${mm}-${dd}`;
let apply = window.localStorage.getItem('apply')
if (apply == "done"){
    $.notify({title :'Success', content:'Your application is sucsessfully added', timeout:5000});
    window.localStorage.setItem('apply','')
}

var count = 2;
// $('#room').selectize()
var t;
function get_room(){
    let formdata = new FormData();
    formdata.append('date',$('#date').val());
    time = '';
    for(x=1;x<count;x++){
        time += $('#time_'+x).val() + ','
    }
    formdata.append('time_slot',time);
    $.ajax({
        url : '../api/free_room_teacher',
        type : 'post',
        data: formdata,
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value },
        cache: false,
        contentType: false,
        processData: false,
        success : function(res){
            console.log(res);
            // $('#room').selectize()[0].selectize.destroy();
            document.getElementById('room').innerHTML= ''
            t = res;
            let option;
            for(x in res){
                option = document.createElement("option");
                option.text = res[x]['__str__'] ;
                option.value = res[x]['id'];
                // if(sel != undefined && x==sel){
                //     option.selected = true;
                // }
                document.getElementById("room").appendChild(option);
            }
            // $('#room').selectize()
    
        },
        error : function(res){
            console.log(res);
        }
    })
}

document.getElementById('form').addEventListener('change',get_room)


function add_another(){
    if(count >3){
        alert("You can't select more than 3.");
        return
    }
    let html = `
    <div class="col col-12">
        <div class="mb-3">
            <label class="form-label" for="room">Time:</label>
            <select id="time_${count}" class= "form-select" placeholder="room_number">
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
                window.localStorage.setItem('apply','done')
                window.location.href = "../apply";
            },
            error: function(res) { console.log(res); }
    
    })
}
)