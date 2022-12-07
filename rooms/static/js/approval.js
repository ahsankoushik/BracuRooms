function get(){


    // let api = new XMLHttpRequest;
    let count = parseInt(document.getElementById("count").value);

    let page = parseInt(document.getElementById("page_count").innerText) ;
    let start= (page-1) * count;

   $.ajax({
    url: '../api/get_booking_approval',
    type: 'GET',
    dataType: 'json',
    success : (function(res){
        console.log(res);
        let html = '';
        for(x in res){
            // console.log(res[x].faculty);
            html += `<tr class="text-center" id ="${res[x].id}">
                <td>${res[x].faculty}</td>
                <td>${res[x].room_number}</td>
                <td>${res[x].date}</td>
                <td>${res[x].time_slot}</td>
                <td><button class="btn btn-success" onClick= "approve(${res[x].id},1)">&#10003;</a></td>
                <td><button class="btn btn-danger" onClick= "approve(${res[x].id},0)"">X</a></td>
            </tr>`;
        }
        document.getElementById('booking_details').innerHTML = html;
    }),
   })
}

get();

document.getElementById("count").addEventListener('change',get);


function approve(id,approval){
    console.log(id,approval);
    $.ajax({
        url:`../api/approve/${id}/${approval}`,
        type:'GET',
        
        success:(function(res){
            // window.location.href = '../apply';
            document.getElementById(id).style.display = 'none'
            let faculty = document.getElementById(id).children[0].innerText
            if (approval == 1){
                $.notify({title :'Approved', content:'The application of '+faculty +' is approved', timeout:5000});
            }else{
                $.notify({title :'Rejected', content:'The application of '+faculty +' is rejected', timeout:5000});
            }
            
        }),
        error: (function(e){
            console.log('error');
            console.log(e);
        })

    })

}


function nextpage(){
    let page = parseInt(document.getElementById("page_count").innerText);
    let total = parseInt(document.getElementById("total").value);
    let count = parseInt(document.getElementById("count").value);
    console.log((page*count),total+count)
    if((page*count)<(total+count)){
        document.getElementById("page_count").innerText = page+1;
        get(); 
    }else{
        console.log("end of page")
    }  
}

function prevpage(){
    let val = parseInt(document.getElementById("page_count").innerText);
    if(val==1){
        console.log('This is the first page')
    }else{
        document.getElementById("page_count").innerText = val-1;
        get();
    }

}