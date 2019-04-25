$(document).ready(function() {
var staged = 1;
var staged2 = 2;
var staged3 = 3;
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
	
    var img = $('img');
    var modalimage = document.getElementById('modalimagex');
    var modalthisimage = document.getElementById('imagethis');
	var topmodals = document.getElementsByClassName('topmodals');
	var trashy = document.getElementsByClassName('trashy');
	var unlocky = document.getElementsByClassName('unlocky');
	var locky = document.getElementsByClassName('locky');
	var navbarphoto = document.getElementsByClassName('navbarphoto');
	var innerimage = document.getElementsByClassName('innerimage');

	
	
	$('img.topmodals').click(function() {
	    alert("you've pressed topmodals");
        return;
	    });
	$('img.trashy').click(function() {
	    console.log("define post for trash");
        console.log("confirmed url for reference to delete: "+this.src);
        var deleted_element =  $(this).attr("id");
        console.log("div id to be deleted "+deleted_element);
        var target = deleted_element.substring(9);
        console.log("post id as target for django to remove from db: "+target);
        var post_del = document.getElementById('div@'+target);
            //delete div from blog www
			//post_del.style.display = 'none';
        post_del.parentNode.removeChild(post_del);
        console.log("div has been deleted: "+post_del);
            //implement here bootstrap place holder with dismissable popup
        alert("post removed");
         var urlx =  '/mydiabprod/postremove/';
		djangoajax(target, urlx);    
        var csrftoken = getCookie('csrftoken');
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
    });
    
    
    $('img.unlocky').click(function(){
         alert("post publicly available");
	});
	
    $('img.locky').click(function(){
         alert("post publicly available");
    });

    $('img.navbarphoto').click(function(){
	//var plex = document.getElementById("showfortogglex");
	    console.log("tooggle dropdown");
		//$("#innertextcontainer").empty();
			//var xx = plex.getArrtibute('display');
       var plex = document.getElementById("showfortogglex");
        var xx = $("#showfortogglex").css("display");
        if (xx == 'none') {
            console.log("check ddplex: "+xx);
            plex.style.display = "block";
        }   else {
            console.log("check ddplex: "+xx);
            plex.style.display = "none";
        }
		/*alert("cleaned");
		var csrftoken = getCookie("csrftoken");
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
		var urlx =  "{% url 'mydiabprod:getpostx' %}";
		var target = "get_post";
        $.ajax({
            url: urlx,
            headers: {"X-CSRFToken":csrftoken},
            type: "POST",
            data: {"target": target},
            success: function(poka) {
			//console.log(poka);
            $("#innertextcontainer").append(poka);
            }
        });*/
		
        return;
    });

    $('img.innerimage').click(function(){
        alert("thisis it");
            //img = $(this);
            //var captionText = getElementById('captionx');
        console.log("defined image: "+this.url);
            //console.log("defined this:" +$(this))
        console.log("file name "+this.src);
        modalimage.style.display = "block";
        modalthisimage.src =  this.src;
    });
	wwx = document.getElementsByClassName("privpadlock");
    $('img.privpadlock').click(function() {
	if (this.classList == 'privpadlock') {
	  //  if (this.src == makeprivatepost.src) {
	    alert("implementing  settings private permission to post");
        console.log("define post for closed privacy");
        console.log("confirmed url for reference to pivacy update: "+this.src);
        var private_element =  $(this).attr("id");
        console.log("div id for public post "+private_element);
        var target = private_element.substring(11);
        console.log("post id as target for django to set is_private in db: "+target);
        console.log("html for that post: "+$(this).attr("src"));
        var newaddress = '/static/mydiabprod/padlock_redd.ico';
		$(this).attr("src", newaddress);
		var newclass = "publicpadlock";
		//$(this).removeClass("privpadlock").addClass("publicpadlock");
		this.classList.remove("privpadlock");
		this.classList.add("publicpadlock");
		$(this).attr("id", "publicmake"+target);
		$(this).attr("data", "@"+target);
		
        var urlx =  '/mydiabprod/postsetprivate';
		djangoajax(target, urlx);	
		} else {
		alert("implementing  settings public permission to post");
        console.log("define post for public privacy");
        console.log("confirmed url for reference to pivacy update: "+this.src);
        var public_element =  $(this).attr("id");
        console.log("div id for public post "+public_element);
        var target = public_element.substring(10);
        console.log("post id as target for django to set is_public in db: "+target);
            //$(this).empty();
        console.log("html for that post: "+$(this).attr("src"));
	    var newaddressx = '/static/mydiabprod/padlock_green.ico';
        $(this).attr("src", newaddressx);
		var newclassx = "privpadlock";
		//$(this).removeClass("publicpadlock").addClass("privpadlock");
		this.classList.remove("publicpadlock");
		this.classList.add("privpadlock");
		$(this).attr("id", "privatemake"+target);
        var urlx =  '/mydiabprod/postsetpublic';
		djangoajax(target, urlx);   
        		}
       //};	
	//   return $(".publicpadlock");
    });
	var ppx = document.getElementsByClassName("publicpadlock");
	$('img.publicpadlock').click(function(){
	if (this.classList == 'publicpadlock') {
	//    if (this.src == makepublicpost.src) {
        alert("implementing  settings public permission to post");
        console.log("define post for public privacy");
        console.log("confirmed url for reference to pivacy update: "+this.src);
        var public_element =  $(this).attr("id");
        console.log("div id for public post "+public_element);
        var target = public_element.substring(10);
        console.log("post id as target for django to set is_public in db: "+target);
            //$(this).empty();
        console.log("html for that post: "+$(this).attr("src"));
	    var newaddressx = '/static/mydiabprod/padlock_green.ico';
        $(this).attr("src", newaddressx);
		var newclassx = "privpadlock";
		//$(this).removeClass("publicpadlock").addClass("privpadlock");
		this.classList.remove("publicpadlock");
		this.classList.add("privpadlock");
		$(this).attr("id", "privatemake"+target);
           
        var urlx =  '/mydiabprod/postsetpublic/';
		djangoajax(target, urlx); 
	//	};
	} else {
	   alert("implementing  settings private permission to post");
        console.log("define post for closed privacy");
        console.log("confirmed url for reference to pivacy update: "+this.src);
        var private_element =  $(this).attr("id");
        console.log("div id for public post "+private_element);
        var target = private_element.substring(11);
        console.log("post id as target for django to set is_private in db: "+target);
        console.log("html for that post: "+$(this).attr("src"));
        var newaddress = '/static/mydiabprod/padlock_redd.ico';
		$(this).attr("src", newaddress);
		var newclass = "publicpadlock";
		//$(this).removeClass("privpadlock").addClass("publicpadlock");
		this.classList.remove("privpadlock");
		this.classList.add("publicpadlock");
		$(this).attr("id", "publicmake"+target);
		var urlx =  '/mydiabprod/postsetprivate';
		djangoajax(target, urlx);
		}
//	 return $(".privpadlock");
	});

	
    //var trashpart = document.getElementById("trashpost");
    //var padlockpriv = document.getElementById("privatemake");
    //var padlockpub = document.getElementById("publicmake");
    //var publicview = document.getElementById("publicpad");
    //var privview = document.getElementById("privpad");
    //var settings_navbar = document.getElementById("settings_navbarx");
    //var plex = document.getElementById("showfortogglex");
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() { 
        modalimage.style.display = "none";
        $("#imagethis").empty();
    }
	function djangoajax(target, urlx) {
	    var csrftoken = getCookie("csrftoken");
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
        $.ajax({
            url: urlx,
            headers: {"X-CSRFToken":csrftoken},
            type: "POST",
            data: {"target": target},
            success: function(text) {
				//console.log("html for that post: "+this.innerHTML);
                //$(el).summernote('editor.insertImage', url);
                //optional tasks here
                //$("#counter").append("</br><p>image</p></br><p><img  alt='Smiley face' height='200' width='300' src="+url+"/></p>");
				//this.innerHTML = "<img id='privatemake' data='priv@{{result.id}}' src='{% static "mydiabprod/padlock_green.ico" %}' height=24; width=24; style='display:none'/>";
            console.log("ajax loaded, django db updated, response sent back: "+text);				
            }
        });
		}
});