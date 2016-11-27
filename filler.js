//currently just makes a stupid table of numbers, needs to be filled with the first 5 entries of the database


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