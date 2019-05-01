

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
$('#portrait_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:15px;width:99%" onclick="fullreader()">'+
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
$('#landscape_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:25px;width:99%" onclick="fullreader()">'+
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
			"<img src='/static/mydiabprod/arrow-97-32.ico' style='padding-left:3px' onclick='fullreadernext(1,"+toreader.id+")'/>"+
			" <img src='/static/mydiabprod/arrow-32-32.ico' style='padding-left:3px' onclick='fullreadernext(2,"+toreader.id+")' /></p></div></div>"+
			"<br><div class='container' id="+toreader.id+" style='padding-top:10px;font-size:14px'"+
			"onClick='this.contentEditable=\"true\";'>"+toreader.html+"</div>"+
			"<div class='row' style='padding-top:15px;padding-bottom:15px;padding-right:15px;border-top:0.5px solid #e3edf2'>"+
			"<button class='button-wjs-blue' id='pex'"+toreader.id+" value='"+toreader.id+"' onclick='blue()'>save</button></div></div>");
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
            $("#innertextcontainer").empty();
			var toreader = JSON.parse(poka);
//var fetty = jsondata;
            $("#innertextcontainer").append("<div class='container'>"+
			"<div class='row' style='padding-top:20px;font-weight:bold;font-size:16px'>"+
			"<div class='col-6'><p style='float:left'>"+toreader.title+"</p></div><div class='col-6'><p style='float:right'>"+
			"<img src='/static/mydiabprod/arrow-97-32.ico' style='padding-left:3px' onclick='fullreadernext(1,"+toreader.id+")' />"+
			" <img src='/static/mydiabprod/arrow-32-32.ico' style='padding-left:3px' onclick='fullreadernext(2,"+toreader.id+")' /></p></div></div>"+
			"<br><div class='container' id="+toreader.id+" style='padding-top:10px;font-size:14px'"+
			"onClick='this.contentEditable=\"true\";'>"+toreader.html+"</div>"+
			"<div class='row' style='padding-top:15px;padding-bottom:15px;padding-right:15px;border-top:0.5px solid #e3edf2'>"+
			"<button class='button-wjs-blue' id='pex'"+toreader.id+" value='"+toreader.id+"' onclick='blue()'>save</button></div></div>");
            }
        })
		return;
	}

//	$('.shadow-sm').click(function() {
//alert("clicked");fullreader 'href="{% url \'mydiabprod:getpostdisplay\' %}" target="_blank">
//});
