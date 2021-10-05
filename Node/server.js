var http = require("http");
var fs = require("fs");

var server = http.createServer(function(req, res){
    if(req.url === "/"){
        fs.readFile("./public/index.html", "utf-8", function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        });
    }

else{
    res.writeHead(404, {"Content-Type":"text/html"});
    res.end(`404 file not found at ${req.url}`);
}
    
    res.end(`
        
    `)
}).listen(3000)

console.log("Server listening on port 3000");