$("select.searchselector_portrait").change(function(){
var optimizer = $(this).children("option:selected").val();
$(".searchtextoptimizer").empty();
$(".searchtextoptimizer").append("Please enter "+optimizer);
//$("#stextoptimizer1").append("Please enter "+optimizer);
//$("#stextoptimizer2").append("Please enter "+optimizer);
//$("#stextoptimizer3").append("Please enter "+optimizer);

});
