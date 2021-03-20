function delete_key(id)
{
    fetch('http://127.0.0.1:8000/api/keyword/'+id, {
        method: 'DELETE',
    }).then(response => {
    if (response.status !== 200) {
        alert('Network error! '+response.status);
        return;
    }
    response.json().then(function (data) {});
    });
}
function init()
{
    fetch('http://127.0.0.1:8000/api/keyword/', {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
    }).then(response => {
        if (response.status !== 200) {
            alert('Network error! '+response.status);
            return;
        }

        response.json().then(function (data) {
            for(var i=0;i<data.length;++i)
            {
                table_row=$("<tr></tr>");
                table_row.append('<td>'+data[i]['id']+'</td>');
                table_row.append('<td>'+data[i]['name']+'</td>');
                table_row.append('<td>'+data[i]['des']+'</td>');
                button = $('<button class="btn btn-danger delete-btn"></button>').html("Xóa");
                button.attr('index',data[i]['id']);
                cell=$('<td></td>').html(button);
                table_row.append(cell);
                $('#key_table > tbody:first').append(table_row);
            }
            $("button.delete-btn").click(function(){
                id=$(this).attr('index');
                delete_key(id);
                window.location.href = "/dict";
            });
        });
    });
};
$("#submit_key_btn").click(function(){
    name=$("#key").val();
    des=$("#des").val();
    fetch('http://127.0.0.1:8000/api/keyword/', {
        method: 'POST',
        body: JSON.stringify({'name':name,'des':des}),
    }).then(response => {
    if (response.status !== 200) {
        alert('Network error! '+response.status);
        return;
    }
    response.json().then(function (data) {            
        });
    });
    window.location.href = "/dict";
});
init();