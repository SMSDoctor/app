
var table = '';

function f(){
	for(var r = 0; r<9; r++){
		table+='<tr>';
		for(var c = 0; c<9; c++){
			table += '<td>' + c + '</td>';
		}		 
		table +='</tr>';
	}
	document.write('<table border=1>' + table + '</table>');
	console.log('<table border=1>' + table + '</table>');
}

$.ajax({
  type: "POST",
  url: "~/pythoncode.py",
  data: { param: "heeeelo"}

}).done(function( o ) {
   // do something
});
console.log("nice");