

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

return [x.title, x.date, x.author, x.options, x.date1];
//console.log("check leng: "+x.options.length);
});
$("#standard_viewport").empty();
$("#portrait_viewport").empty();
$("#landscape_viewport").empty();
var i = 0;
$.each((pates), function(key, value) { 
i++;
console.log('hold the key: '+value[2]);
var str1 = value[4].replace('T', ' ');
var str2 = str1.substring(0,16);

$('#standard_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:19px;width:99%;font-size:15px">'+
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
$('#portrait_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:15px;width:99%">'+
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
$('#landscape_viewport').append('<div class="shadow-sm p-3 mb-1 rounded" style="line-height:25px;width:99%">'+
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
