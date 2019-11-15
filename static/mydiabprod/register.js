

$("div.firstnames").focusout(function(event) {
	alert("firstname");
});

$("div.lastnames").focusout(function(event) {
	alert("lastname");
});



$("div.usernames").focusout(function(event) {
event.preventDefault();
    var un = $(this).find("input").val();
	var inputs = $(this).find("input");
    console.log("hhhh "+un);
    var csrftoken = getCookie('csrftoken');
	$.ajax({
                url: "/mydiabprod/checkun/",
                headers: {"X-CSRFToken":csrftoken},
                type: "POST",
                data: {'checkun':un},
                success: function(unresponse) {
				console.log('response from django '+ unresponse);
				if ((unresponse !=='passed')) {
				console.log("hhssshh "+un);
				console.log("jjjfas "+inputs);
				$(inputs).focus();
				    alert('username already in use, please choose other or use suggested '+unresponse);
					$(inputs).val('');
					$(inputs).val(unresponse);
					event.stopImmediatePropagation();
					return;
					} else {
                return;
				}}
				
				});
				})
$("div.emails").focusout(function(event) {
	alert("lastname");
});		
$("div.passwords").focusout(function(e) {
e.preventDefault;
//e.stopImmediatePropagation();
    var inputsp = $(this).find("input");
				$(inputsp).css("color", "black");
var passvalidation = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/i;
var passw = $(this).find("input").val();
console.log("password "+passw);
if (passw.match(passvalidation)) {
$("#repasswordrn").focus();
} else if (!passw.match(passvalidation)) {

console.log("poka "+inputsp.val());
alert("password should be corrected");
$(inputsp).val("");
$(inputsp).css("color", "red");
$(inputsp).attr("placeholder", "enter again");

//e.stopImmediatePropagation();

return false;
}

});


$("div.repasswords").focusout(function(event) {
var reinputp = $(this).find("input");
console.log("repass "+reinputp);
var passnx = $("div.passwords").find("input");
console.log("get password "+passnx);
var passn = $("div.passwords").find("input").val();
var un = $(reinputp).val();
console.log("fist is repass "+un);
console.log("second is pass "+passn);
if (un !== passn) {
console.log("enetered repass "+un);
alert("passwords don\'t match, please type again");
$(".button-wjs-account").attr("disabled", true);
$(reinputp).val("");
$(reinputp).css("color", "red");
$(reinputp).attr("placeholder", "enter again");
} else {
$(".button-wjs-account").attr("disabled", false);
$(reinputp).css("color", "black");
return;
}
});

$(".button-wjs-account").click(function(event) {
var firsty = $("div.firstnames").find("input");
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
		
				});
					return false;
})