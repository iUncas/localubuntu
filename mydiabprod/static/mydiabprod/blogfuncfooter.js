
    var csrf = $("meta[name='csrf']").attr("content");  
    function getCookie(name) {
                var cookieValue = null;
             
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                        }
                    }
                }
                return cookieValue;
        }
function fetchnextpage() {
	var forwards = document.getElementById('plusdate');
	var forwardref =  $("#plusdate").attr("data");
    var csrftoken = getCookie('csrftoken');
            console.log("csrf token: "+csrftoken);
            console.log("firing ajax");
			console.log("id for post: "+forwardref);
            $.ajax({
                url: '/mydiabprod:/getforwards',
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {'forward': forwardref},
                success: function(context) {
			    context.map(function(x){

				return console.log("your key: "+x);

				});
                //$(el).summernote('editor.insertImage', url);
                //optional tasks here
                //$("#counter").append("</br><p>image</p></br><p><img  alt='Smiley face' height='200' width='300' src="+url+"/></p>");
                //this.innerHTML = "<img id='privatemake{{result.id}}' data='priv@{{result.id}}' src='{% static "mydiabprod/padlock_redd.ico" %}' height=24; width=24; style='display:none'/>";
                console.log("ajax loaded, django db updated, response sent back: ");
                $("#innertextcontainer").empty();
                $("#innertextcontainer").load(" #innertextcontainer");			
                }
            });
	
	}