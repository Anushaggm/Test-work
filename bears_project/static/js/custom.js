/**
 * Created by anusha on 28/10/18.
 */
function getCookie(name) {
 var value = "; " + document.cookie;
 var parts = value.split("; " + name + "=");
 if (parts.length == 2) return parts.pop().split(";").shift();
}


//......................create bear.............................................//
$('#create_bear').click(
    function()
    {
       var name = $('#name').val();
       var bear_type = $('#bear_type').val();
        var $csrfmiddlewaretoken  = getCookie('csrftoken');
        if ($csrfmiddlewaretoken == undefined)
                {
                    $csrfmiddlewaretoken = $('#csrf').val();
                }
        $('#span_name').text('');
        $('#span_bear_type').text('');
        $('#span_success').text('');
        $('#span_failure').text('');
        var $status=1;
        if(name.length==0)
        {
            $('#span_name').text('Required Field');
            $status =0;
        }
        if(name.length>50)
        {
            $('#span_name').text('Name should be less than 50 characters');
            $status =0;
        }
        if(bear_type.length==0)
        {
            $('#span_bear_type').text('Required Field');
            $status =0;
        }
         if ($status==1) {
            //preparing form data
           var data = new FormData()
           data.append('name',name);
           data.append('bear_type',bear_type);
           // ajax method
           $.ajax({
               data: data,
               type: "POST",
               url:  window.location.pathname,
               dataType: 'json',
               processData: false, // Don't process the files
               contentType: false,
               beforeSend: function (xhr, settings) { // to send csrf token
                   xhr.setRequestHeader("X-CSRFToken", $csrfmiddlewaretoken);
               },
               success: function (data) { // on success..
                    if (data.status==true)
                    {
                        $('#span_success').text('You hve successfully created a Bear');
                        $('#span_success').fadeIn().delay(5000).fadeOut();
                        window.setTimeout(function(){
                         window.location = "i-love-bears";
                     }, 2000)

                    }
                   else if (data.status == false){
                        if (data.exist == true){
                            $('#span_failure').text('A bear with same name and type already exists!');
                        }
                        else {
                            $('#span_failure').text('Some error occurs.Please submit all the data!');
                        }
                        $('#span_failure').fadeIn().delay(5000).fadeOut();

                    }
               },
               error: function (data) { //calls when internal server error occurs.
               }
           });
       }
    });
