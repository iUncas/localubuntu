

function searchaction() {
		$("#innertextcontainer").empty();

	    console.log("cleaned");
		var csrftoken = getCookie("csrftoken");
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
		var urlx =  "/mydiabprod/getpostx/";
		var target = "get_post";
        $.ajax({
            url: urlx,
            headers: {"X-CSRFToken":csrftoken},
            type: "POST",
            data: {"target": target},
            success: function(poka) {
			//console.log(poka);
				var plex = document.getElementById("showfortogglex");
             plex.style.display = "none";
            $("#innertextcontainer").append(poka);
            }
        })
		return;
    }


function registeraction() {
		$("#innertextcontainer").empty();

	    console.log("cleaned");
		var csrftoken = getCookie("csrftoken");
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
		var urlx =  "/mydiabprod/registerx/";
		var target = "get_post";
        $.ajax({
            url: urlx,
            headers: {"X-CSRFToken":csrftoken},
            type: "POST",
            data: {"target": target},
            success: function(poka) {
			//console.log(poka);
				var plex = document.getElementById("showfortogglex");
             plex.style.display = "none";
            $("#innertextcontainer").append(poka);
            }
        })
		return;
    }	




function uploadjson(jsondata) {
//$.getJSON("/mydiabprod/getsearch/", {"parameter":1}, function(loadup) {
//	var testalert = JSON.parse(loadup);
//    alert(testalert);
//});
//var dane = $.getJSON( 'file:///C:/Users/a574788/Desktop/HP%20deploy/getjson.txt');
console.log(jsondata);
var fetty = JSON.parse(jsondata);
//var fetty = jsondata;
var pates = fetty.map(function(x) {

return [x.title, x.date, x.author, x.options, x.date1, x.constructionid];
//console.log("check leng: "+x.options.length);
});
$('#topsearchlabel').empty();
$('#topsearchlabel').append('following results have been found in blog database');
$("#standard_viewport").empty();
$("#portrait_viewport").empty();
$("#landscape_viewport").empty();
var i = 0;
$.each((pates), function(key, value) { 
i++;
console.log('hold the key: '+value[2]);
var str1 = value[4].replace('T', ' ');
var str2 = str1.substring(0,16);

$('#standard_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:19px;width:99%;font-size:15px"'+
' id="'+value[5]+'" onclick="fullreader('+value[5]+')">'+
'<div class="row">'+
'<div class="col-3" style="padding-left:25px">'+
'<div class="row">'+
'<p style="font-size:16px;font-weight:bold">'+value[0]+'</p>'+
'</div>'+
'<div class="row">'+
'<p style="font-size:13px; font-style:oblique">'+str2+'</p>'+
'</div>'+
'</div>'+
'<div class="col-2">'+
'<p>'+value[2]+'</p>'+
'</div>'+
'<div class="col-5">'+
'<p>'+value[1]+'</p>'+
'</div>'+
'<div class="col-2">'+
'<p>'+value[3]+'</p>'+
'</div>'+
'</div>'+
'</div>');
$('#portrait_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:15px;width:99%"'+
' id="'+value[5]+'" onclick="fullreader('+value[5]+')">'+
'<div class="col-12">'+
'<div class="row">'+
'<p style="font-weight:bold">'+value[0]+'</p>'+
'</div>'+
'<div class="row">'+
'<p style="font-size:13px; font-style:oblique">by '+value[2]+'</p>'+
'</div>'+
'<div class="row">'+
'<p style="font-size:13px">'+value[1]+'</p>'+
'</div>'+
'<div class="row">'+
'<p>'+value[3]+'</p>'+
'</div>'+
'</div>'+
'</div>');
$('#landscape_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:25px;width:99%"'+
' id="'+value[5]+'" onclick="fullreader('+value[5]+')">'+
'<div class="row">'+
'<div class="col-3" style="padding-left:25px">'+
'<div class="row">'+
'<p style="font-weight: bold">'+value[0]+'</p>'+
'</div>'+
'<div class="row">'+
'<p style="font-size:12px; font-style:oblique">'+str2+'</p>'+
'</div>'+
'</div>'+
'<div class="col-2">'+
'<p style="font-size:12px">by '+value[2]+'</p>'+
'</div>'+
'<div class="col-5">'+
'<p style="font-size:12px">'+value[1]+'</p>'+
'</div>'+
'<div class="col-2">'+
'<p>'+value[3]+'</p>'+
'</div>'+
'</div>'+
'</div>');
});
}

function fullreader(constructionid) {
	alert("clicked");
	//var constructionid = construction.substring(5);
	var urlx =  "/mydiabprod/getpostdisplay/";
	var csrftoken = getCookie("csrftoken");
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
        $.ajax({
            url: urlx,
            headers: {"X-CSRFToken":csrftoken},
            type: "POST",
            data: {"constructionid": constructionid},
            success: function(poka) {
            $("#innertextcontainer").empty();
			var toreader = JSON.parse(poka);
//var fetty = jsondata;
            $("#innertextcontainer").append("<div class='container'>"+
			"<div class='row' style='padding-top:20px;font-weight:bold;font-size:16px'>"+
			"<div class='col-6'><p style='float:left'>"+toreader.title+"</p></div><div class='col-6'><p style='float:right'>"+
			"<img src='/static/mydiabprod/arrow-96-33.ico' style='padding-left:3px' onclick='fullreadernext(1,"+toreader.id+")' id='backarrow'"+
			" alt='previous post'/>"+
			" <img src='/static/mydiabprod/arrow-33-32.ico' style='padding-left:3px' onclick='fullreadernext(2,"+toreader.id+")' id='forwardarrow'"+ 
			" alt='next post'/></p></div></div>"+
			"<br><div class='posthtml' id="+toreader.id+" style='padding-top:10px;font-size:14px'"+
			"onClick='this.contentEditable=\"true\";'>"+toreader.html+"</div>"+
			"<div class='row' style='padding-top:15px;padding-bottom:15px;padding-right:15px;border-top:0.5px solid #e3edf2'>"+
			"<button class='button-wjs-blue' id='pex'"+toreader.id+" value='"+toreader.id+"' onclick='blue()'>save</button></div></div>");
			if ($('img')) {
			$('.posthtml img').attr('class', 'innerimage');
		    $('.posthtml img').attr('alt', 'innerimagex');
			}
		}
        })
		return;
	}
	function blue() {
		var intsx = $('.button-wjs-blue').attr('value');
	
//$('.button-wjs-blue').click(function() {
//event.preventDefault;
//var intsx = $(this).attr('value');
var pex = $("#"+intsx).html();
alert("OK");
console.log("first value:"+pex);

var urlx =  "/mydiabprod/updatepost/";
	var csrftoken = getCookie("csrftoken");
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
        $.ajax({
            url: urlx,
            headers: {"X-CSRFToken":csrftoken},
            type: "POST",
            data: {"postupdateid": intsx, "postupdatehtml":pex},
            success: function(text) {
            alert(text);
            }
        })
		return;
}

function fullreadernext(texty,constructionid) {
	alert("clicked");
	//var constructionid = construction.substring(5);
	var urlx =  "/mydiabprod/getpostdisplaynext/";
	var csrftoken = getCookie("csrftoken");
        console.log("csrf token: "+csrftoken);
        console.log("firing ajax");
		if (texty==1) {
		control='firsty';
		} else if (texty==2) {
			control='secondy';
		}
		console.log("get this stuff "+control);
        $.ajax({
            url: urlx,
            headers: {"X-CSRFToken":csrftoken},
            type: "POST",
            data: {"constructionid": constructionid, "control": control},
            success: function(poka) {
            if (poka=='no results to show') {
				alert('no more results, please go back');
				$('#backarrow').attr('src', '/static/mydiabprod/arrow-96-32.ico');
				//$('#backarrow').css('width', '24px');
				//$('#backarrow').css('height', '24px');
			} else if (poka == 'no resultsx to show') {
				alert('no more results, please go back');
				$('#forwardarrow').attr('src', '/static/mydiabprod/arrow-31-32.ico');
				//$('#forwardarrow').css('width', '24px');
				//$('#forwardarrow').css('height', '24px');
			} else {
            $("#innertextcontainer").empty();
			var toreader = JSON.parse(poka);
//var fetty = jsondata;
            $("#innertextcontainer").append("<div class='container'>"+
			"<div class='row' style='padding-top:20px;font-weight:bold;font-size:16px'>"+
			"<div class='col-6'><p style='float:left'>"+toreader.title+"</p></div><div class='col-6'><p style='float:right'>"+
			"<img src='/static/mydiabprod/arrow-96-33.ico' style='padding-left:3px' onclick='fullreadernext(1,"+toreader.id+")' id='backarrow'"+
            " alt='previous post' />"+
			" <img src='/static/mydiabprod/arrow-33-32.ico' style='padding-left:3px' onclick='fullreadernext(2,"+toreader.id+")' id='forwardarrow'"+
			" alt='next post' /></p></div></div>"+
			"<br><div class='posthtml' id="+toreader.id+" style='padding-top:10px;font-size:14px'"+
			"onClick='this.contentEditable=\"true\";'>"+toreader.html+"</div>"+
			"<div class='row' style='padding-top:15px;padding-bottom:15px;padding-right:15px;border-top:0.5px solid #e3edf2'>"+
			"<button class='button-wjs-blue' id='pex'"+toreader.id+" value='"+toreader.id+"' onclick='blue()'>save</button></div></div>");
			if ($('img')) {
			$('.posthtml img').attr('class', 'innerimage');
		    $('.posthtml img').attr('alt', 'innerimagex');
			}
            }}
        });
		
		
		return;
	}

//	$('.shadow-sm').click(function() {
//alert("clicked");fullreader 'href="{% url \'mydiabprod:getpostdisplay\' %}" target="_blank">
//});





function firstnames() {
console.log("firstnames");
 var un = $("input[placeholder='firstname']").val();
	//var inputs = $(this).find("input");
    console.log("hhhh "+un);
return;
}
function lastnames() {
console.log("lastnames");
var un = $("input[placeholder='lastname']").val();
	//var inputs = $(this).find("input");
    console.log("hhhh "+un);
return false;
}
function usernames() {
console.log("usernames");
var usernamenr = $("input[placeholder='username']").val();
//var takeinput = $("input[placeholder='username']");
var takeinput = $("div.usernames").find("input");
var emailinput = $("input[placeholder='email']");
    console.log("your username "+usernamenr);
	var csrftoken = getCookie('csrftoken');
	if ( usernamenr == "") {
		return;
	} else {
	$.ajax({
                url: "/mydiabprod/checkun/",
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {'checkun':usernamenr},
                success: function(unresponse) {
				console.log('response from django '+ unresponse);
				if (unresponse =='passed') {
					//$('[data-toggle="tooltip1"]').tooltip("destroy");
				return;
					} else {
				    $('[data-toggle="tooltip1"]').tooltip();
                    var newusername = String(unresponse);				    
				    console.log('username already in use, please choose other or use suggested '+unresponse);
					$(takeinput).val('');
					$(takeinput).val(newusername);
					$(takeinput).focus();
					console.log("taken");
					return false;
					
				}}
				
				});
	}
return false;
}
function emails() {
console.log("emails");

var emailinput = $("input[placeholder='email']");
var emailinputval = $("input[placeholder='email']").val();
var inputsp = $("input[placeholder='password']");
var emailvalidator =  /^([\w-(?=\.)])*\@{1}[a-zA-Z0-9\-\_]*\.[a-z]{2,3}/i;
console.log(emailinputval);
if (emailinputval.match(emailvalidator)) {
	//$('[data-toggle="tooltip2"]').tooltip("destroy");
//$(inputsp).focus();
return;
} else if ( emailinputval == "") {
return false;
} else 	{
	$('[data-toggle="tooltip2"]').tooltip();
$(emailinput).focus();
console.log("poka "+emailinput.val());
console.log("email should be corrected");
$(emailinput).val("");
return false;
}
return false;
}
function passwords() {
	
console.log("passwords");
	    var inputsp = $("input[placeholder='password']");
		var repass = $("input[placeholder='retype password']");
				$(inputsp).css("color", "black");
var passvalidation = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/i;
var passw = $(inputsp).val();
console.log("password "+passw);
if (passw == "") {
	//$('[data-toggle="tooltip3"]').tooltip();
	return;
 } else if (passw.match(passvalidation)) {
//$(repass).focus();
//$('[data-toggle="tooltip3"]').tooltip("destroy");
return;
} else  {
	  $('[data-toggle="tooltip3"]').tooltip();
	 // $("#passwords").tooltip("toggle");
$(inputsp).focus();
console.log("poka "+inputsp.val());
console.log("password should be corrected");
$(inputsp).val("");
$(inputsp).css("color", "red");
return;
}
	
return false;
}
function repaswords() {
console.log("repasswords");
var un = $("input[placeholder='retype password']").val();
var reinputp = $("input[placeholder='retype password']");
var passn = $("input[placeholder='password']").val();
console.log("fist is repass "+un);
console.log("second is pass "+passn);
   if (un == "") {
	   return false;
  } else if (un == passn) {
$(".button-wjs-account").attr("disabled", false);
$(reinputp).css("color", "black");
return;
} else {
$(reinputp).focus();
console.log("enetered repass "+un);
console.log("passwords don\'t match, please type again");
$(".button-wjs-account").attr("disabled", true);
$(reinputp).val("");
$(reinputp).css("color", "red");
}
return false;
}

$(".button-wjs-account").click(function(event) {
	printJS('topcontainer', 'html');
/*var firsty = $("div.firstnames").find("input");
var fn = $(firsty).val();
console.log("pay to" +fn);
secondss = $("div.lastnames").find("input");
var ln =  $(secondss).val();
console.log("pay to" +ln);
var thirds = $("div.usernames").find("input");
var un = $(thirds).val();
console.log("pay to" +un);
var fourths = $("div.passwords").find("input");
var passn = $(fourths).val();
console.log("pay to" +passn);
var sixtus = $("div.emails").find("input");
var emn = $(sixtus).val();
console.log("pay to" +emn);
var septus = $("div.repasswords").find("input");
var repassn = $(septus).val();
	var csrftoken = getCookie("csrftoken");
   
	$.ajax({
                url: "/mydiabprod/registerun/",
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {"fn":fn, "ln":ln, "un":un, "passn":passn, "emn":emn},
                success: function(regresponse) {
				//var external = JSON.parse(data);
                //external.map(function(x) {
				//return console.log(x.testx);
				console.log(regresponse);
				alert(regresponse);
				$(firsty).val("");
				$(secondss).val("");
				$(thirds).val("");
				$(fourths).val("");
				$(sixtus).val("");
				$(septus).val("");
				}
		
				});*/
					return false;
})

function portraitfirstnames() {
console.log("firstnames");
 var un = $("div.pufirstnames").find("input");
 console.log(un.val());
	//var inputs = $(this).find("input");
   // console.log("hhhh "+un);
return;
}

function portraitlastnames() {
console.log("lastnames");
var portraitlastname = $("div.pulastnames").find("input");
var un = portraitlastname.val();
	//var inputs = $(this).find("input");
    console.log("hhhh "+un);
return false;
}
function portraitusernames() {
console.log("usernames");
var puname = $("div.punames").find("input");
var forupload = puname.val();
console.log("welcome "+ forupload);
var csrftoken = getCookie('csrftoken');
if ( forupload == "") {
	return false;
} else {
	           $.ajax({
                url: "/mydiabprod/checkun/",
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {'checkun':forupload},
                success: function(unresponse) {
				console.log('response from django '+ unresponse);
				if (unresponse =='passed') {
				return false;
					} else {
				var newusername = String(unresponse);				    
				    console.log('username already in use, please choose other or use suggested '+unresponse);
					puname.val('');
					puname.val(newusername);
					puname.focus();
					console.log("taken");
					return false;
				}}
				
				});
                   }
				

}
function portraitemails() {
console.log("emails");

var emailinput = $("div.puemails").find("input");
var emailinputval = emailinput.val();
var inputsp = $("input[placeholder='password']");
var emailvalidator =  /^([\w-(?=\.)])*\@{1}[a-zA-Z0-9\-\_]*\.[a-z]{2,3}/i;
console.log(emailinputval);
if ( emailinputval == "") {
	return false;
} else if (emailinputval.match(emailvalidator)) {
//$(inputsp).focus();
return;
} else  {
$(emailinput).focus();
console.log("poka "+emailinput.val());
console.log("email should be corrected");
$(emailinput).val("");
return;
}
return false;
}
function portraitpasswords() {
console.log("passwords");
    var inputsp = $("div.pupass").find("input");
	var passw = inputsp.val();
		var repass = $("div.purepass").find("input");
				$(inputsp).css("color", "black");
var passvalidation = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/i;

console.log("password "+passw);
if ( passw == "" ) {
	return false;
} else if (passw.match(passvalidation)) {
//$(repass).focus();
return
} else  {
$(inputsp).focus();
console.log("poka "+inputsp.val());
console.log("password should be corrected");
$(inputsp).val("");
$(inputsp).css("color", "red");
return;
}
	
return false;
}
function portraitrepaswords() {
console.log("repasswords");
var reinputp = $("div.purepass").find("input");
var un = reinputp.val();
var passn1 = $("div.pupass").find("input");
var passn = passn1.val();
console.log("fist is repass "+un);
console.log("second is pass "+passn);
if ( un == "" ) {
	return false;
    } else if (un == passn) {
$(".button-wjs-account").attr("disabled", false);
reinputp.css("color", "black");
return;
} else {
$(reinputp).focus();
console.log("enetered repass "+un);
console.log("passwords don\'t match, please type again");
$(".button-wjs-account").attr("disabled", true);
(reinputp).val("");
(reinputp).css("color", "red");
}
return false;
console.log(un);
}
$(".button-wjs-portrait").click(function(event) {
var firsty = $("div.pufirstnames").find("input");
var fn = firsty.val();
console.log("pay to" +fn);
secondss = $("div.pulastnames").find("input");
var ln =  secondss.val();
console.log("pay to" +ln);
var thirds = $("div.punames").find("input");
var un = thirds.val();
console.log("pay to" +un);
var fourths = $("div.pupass").find("input");
var passn = fourths.val();
console.log("pay to" +passn);
var sixtus = $("div.puemails").find("input");
var emn = sixtus.val();
console.log("pay to" +emn);
var septus = $("div.purepass").find("input");
var repassn = septus.val();
	var csrftoken = getCookie("csrftoken");
   
	$.ajax({
                url: "/mydiabprod/registerun/",
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {"fn":fn, "ln":ln, "un":un, "passn":passn, "emn":emn},
                success: function(regresponse) {
				//var external = JSON.parse(data);
                //external.map(function(x) {
				//return console.log(x.testx);
				console.log(regresponse);
				alert(regresponse);
				firsty.val("");
				secondss.val("");
				thirds.val("");
				fourths.val("");
				sixtus.val("");
				septus.val("");
				}
		
				});
					return false;
})

function landscapefirstnames() {
console.log("firstnames");
 var un = $("div.lafirstn").find("input");
 console.log(un.val());
	//var inputs = $(this).find("input");
   // console.log("hhhh "+un);
return;
}

function landscapelastnames() {
console.log("lastnames");
var portraitlastname = $("div.lalastn").find("input");
var un = portraitlastname.val();
	//var inputs = $(this).find("input");
    console.log("hhhh "+un);
return false;
}
function landscapeusernames() {
console.log("usernames");
var puname = $("div.launm").find("input");
var forupload = puname.val();
console.log("welcome "+ forupload);
var csrftoken = getCookie('csrftoken');
if ( forupload == "" ) {
	return false;
} else {
	$.ajax({
                url: "/mydiabprod/checkun/",
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {'checkun':forupload},
                success: function(unresponse) {
				console.log('response from django '+ unresponse);
				if (unresponse =='passed') {
				return;
					} else {
				var newusername = String(unresponse);				    
				    console.log('username already in use, please choose other or use suggested '+unresponse);
					puname.val('');
					puname.val(newusername);
					puname.focus();
					console.log("taken");
					return false;
				}}
				
				});
            }

}
function landscapemails() {
console.log("emails");

var emailinput = $("div.laemails").find("input");
var emailinputval = emailinput.val();
var inputsp = $("input[placeholder='password']");
var emailvalidator =  /^([\w-(?=\.)])*\@{1}[a-zA-Z0-9\-\_]*\.[a-z]{2,3}/i;
console.log(emailinputval);
if ( emailinputval == "" ) {
	return false;
    } else if (emailinputval.match(emailvalidator)) {
//$(inputsp).focus();
return;
} else  {
$(emailinput).focus();
console.log("poka "+emailinput.val());
console.log("email should be corrected");
$(emailinput).val("");
return;
}
return false;
}
function landscapepasswords() {
console.log("passwords");
    var inputsp = $("div.lapass").find("input");
	var passw = inputsp.val();
		var repass = $("div.larepass").find("input");
				$(inputsp).css("color", "black");
var passvalidation = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/i;

console.log("password "+passw);
if ( passw == "" ) {
	return false;
    } else if (passw.match(passvalidation)) {
//$(repass).focus();
return
} else  {
$(inputsp).focus();
console.log("poka "+inputsp.val());
console.log("password should be corrected");
$(inputsp).val("");
$(inputsp).css("color", "red");
return;
}
	
return false;
}
function landscaperepaswords() {
console.log("repasswords");
var reinputp = $("div.larepass").find("input");
var un = reinputp.val();
var passn1 = $("div.lapass").find("input");
var passn = passn1.val();
console.log("fist is repass "+un);
console.log("second is pass "+passn);
if ( un == "") {
	return false;
    } else if (un == passn) {
$(".button-wjs-account").attr("disabled", false);
reinputp.css("color", "black");
return;
} else {
$(reinputp).focus();
console.log("enetered repass "+un);
console.log("passwords don\'t match, please type again");
$(".button-wjs-account").attr("disabled", true);
(reinputp).val("");
(reinputp).css("color", "red");
}
return false;
console.log(un);
}

$(".button-wjs-landscape").click(function(event) {
var firsty = $("div.lafirstn").find("input");
var fn = firsty.val();
console.log("pay to" +fn);
secondss = $("div.lalastn").find("input");
var ln =  secondss.val();
console.log("pay to" +ln);
var thirds = $("div.launm").find("input");
var un = thirds.val();
console.log("pay to" +un);
var fourths = $("div.lapass").find("input");
var passn = fourths.val();
console.log("pay to" +passn);
var sixtus = $("div.laemails").find("input");
var emn = sixtus.val();
console.log("pay to" +emn);
var septus = $("div.larepass").find("input");
var repassn = septus.val();
	var csrftoken = getCookie("csrftoken");
   
	$.ajax({
                url: "/mydiabprod/registerun/",
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {"fn":fn, "ln":ln, "un":un, "passn":passn, "emn":emn},
                success: function(regresponse) {
				//var external = JSON.parse(data);
                //external.map(function(x) {
				//return console.log(x.testx);
				console.log(regresponse);
				alert(regresponse);
				firsty.val("");
				secondss.val("");
				thirds.val("");
				fourths.val("");
				sixtus.val("");
				septus.val("");
				}
		
				});
					return false;
})

function peska() {
	console.log("alert for user");
	$("div.usernames").find("input").focus();
}