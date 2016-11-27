var http = require('http');
var fs = require('fs');
var url = require('url');
var db = require('./db.js');

//creating instance of the server
http.createServer(function(request, response){
    var path = url.parse(request.url).pathname;
    fs.readFile(path.substr(1), function(err,data){
        if (err){
           //print error page
           response.writeHead(404, {'Content-Type': 'text/html'});
        } else {
          //print html page
           response.writeHead(200, {'Content-Type': 'text/html'});
           response.write(data.toString());
        }
        response.end();
    });
}).listen(8080);

console.log('Server running at http://127.0.0.1:8080/');
