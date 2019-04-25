

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
            $("#innertextcontainer").append(poka);
            }
        })
		return;
    }





function uploadjson() {
$.getJSON("/mydiabprod/getsearch/", {"parameter":1}, function(loadup) {
	var testalert = JSON.parse(loadup);
    alert(testalert);
});
//var dane = $.getJSON( 'file:///C:/Users/a574788/Desktop/HP%20deploy/getjson.txt');
console.log(dane);
var fetty = JSON.parse(dane);
var pates = fetty.map(function(x) {

return [x.title, x.date, x.author, x.options];
//console.log("check leng: "+x.options.length);
});
$("#standard_viewport").empty();
$("#portrait_viewport").empty();
$("#landscape_viewport").empty();
var i = 0;
$.each((pates), function(key, value) { 
console.log('hold the key: '+value[2]);
$('#standard_viewport').append('<div class="shadow-sm p-3 mb-1 bg-white rounded" style="line-height:5px;width:99%" >'+
'<div class="row">'+
'<div class="col-2">'+
'<p>'+value[0]+'</p>'+
'</div>'+
'<div class="col-2">'+
'<p>'+value[2]+'</p>'+
'</div>'+
'<div class="col-4">'+
'<p>'+value[1]+'</p>'+
'</div>'+
'<div class="col-4">'+
'<p>'+value[3]+'</p>'+
'</div>'+
'</div>'+
'</div>');
$('#portrait_viewport').append('<div class="shadow-sm p-3 mb-1 bg-white rounded" style="line-height:15px;width:99%" >'+
'<div class="col-12">'+
'<div class="row">'+
'<p>'+value[0]+'</p>'+
'</div>'+
'<div class="row">'+
'<p>'+value[2]+'</p>'+
'</div>'+
'<div class="row">'+
'<p>'+value[1]+'</p>'+
'</div>'+
'<div class="row">'+
'<p>'+value[3]+'</p>'+
'</div>'+
'</div>'+
'</div>');
$('#landscape_viewport').append('<div class="shadow-sm p-3 mb-1 bg-white rounded" style="line-height:25px;width:99%" >'+
'<div class="row">'+
'<div class="col-2">'+
'<p>'+value[0]+'</p>'+
'</div>'+
'<div class="col-2">'+
'<p>'+value[2]+'</p>'+
'</div>'+
'<div class="col-4">'+
'<p>'+value[1]+'</p>'+
'</div>'+
'<div class="col-4">'+
'<p>'+value[3]+'</p>'+
'</div>'+
'</div>'+
'</div>');
});
}
