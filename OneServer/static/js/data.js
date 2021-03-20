function init()
{
    fetch('http://127.0.0.1:8000/api/data/', {
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
                button = $('<button class="btn btn-success download-btn"></button>').html("Tải xuống");
                button.attr('name',data[i]['name']);
                cell=$('<td></td>');
                cell.append(button);
                button = $('<button class="btn btn-danger delete-btn"></button>').html("Xóa");
                button.attr('id',data[i]['id']);
                cell.append(button);
                table_row.append(cell);
                $('#data_table > tbody:first').append(table_row);
            }
            $("button.download-btn").click(function(){
                name=$(this).attr('name');
                alert(name);
                window.location.href = "/api/download/"+name+'/';
            });
            $("button.delete-btn").click(function(){
                id=$(this).attr('id');
                fetch('http://127.0.0.1:8000/api/data/', {
                method: 'DELETE',
                body: JSON.stringify({'id':id}),
                }).then(response => {
                if (response.status !== 204) {
                    alert("Lỗi kết nối "+response.status);  
                    return;
                } else 
                {
                    alert("Xóa thành công!");
                    window.location.href = "/data";
                }
                response.json().then(function (data) {});
                });
            });
        });
    });
};
init();
$("#upload_data_form").submit(function(event){
    event.preventDefault();
    var input=document.getElementById("file1");
    //var input = document.querySelector('input[type="file"]');
    var des=$("#des").val();
    var formData = new FormData();
    formData.append('file', input.files[0]);
    formData.append('des', des);
    fetch('http://127.0.0.1:8000/api/data/', {
        method: 'POST',
        body: formData,
    }).then(response => {
    if (response.status !== 200) {
            alert("Lỗi kết nối "+response.status);
            return;
        } else 
        {
            alert("Tải lên thành công!");
            window.location.href = "/data";
        }
        response.json().then(function (data) {
        });
    });
});