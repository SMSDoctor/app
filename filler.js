//gains access to db functions
var db = require('./db.js');

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
}
