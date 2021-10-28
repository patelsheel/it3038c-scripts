var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");

function serverUptime() {
    uptime = os.uptime();
    days = Math.floor(uptime / 86400);
    hours = Math.floor(uptime % (86400) / 3600);
    minutes = Math.floor(uptime % 3600 / 600);
    seconds = Math.floor(uptime % 3600 % 60);
    return ` ${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds} Seconds`;
}

http.createServer(function (req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "utf-8", function (err, body) {
            res.writeHead(200, {
                "Content-Type": "text/html"
            });
            res.end(body);
        });
    } else if (req.url.match("/sysinfo")) {
        myHostName = os.hostname();
        totalMemory = ((os.totalmem()) / 1048576); //Adding "1048576" value to convert from Byte to MB **Found it on Stackoverflow.
        freeMemory = ((os.freemem()) / 1048576);
        totalCPUs = os.cpus().length; //Adding .length to get a number insted of full CPU information.
        html = `
        <!DOCTYPE html>
        <html>
            <head> 
                <title> Node js </title> </head> 
                    <body> 
                    <p>Hostname: ${myHostName}</p>
                    <p>IP: ${ip.address()} </p>
                    <p>Server Uptime:${serverUptime()} </p>
                    <p>Total Memory: ${totalMemory} MB </p>
                    <p>Free Memory: ${freeMemory} MB </p>
                    <p>Number of CPU's: ${totalCPUs} </p>
                    </body>
        </html>
        `
        res.writeHead(200, {
            "Content-Type": "text/html"
        });
        res.end(html);
    } else {
        res.writeHead(404, {
            "Content-Type": "text/plain"
        });
        res.end(`404 file not found at ${req.url}`);
    }
}).listen(3000)

console.log("Server listening on port 3000");