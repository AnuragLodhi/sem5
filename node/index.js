const http = require('http')
const fs = require('fs')

const PORT = 5500

const getFile = (path) => {
    return new Promise((resolve, reject) => {
        try {
            const file = fs.readFileSync("./app" + path + "/page.html");
            resolve(Buffer.from(file.toString()));
        } catch(err) {
            console.log(err);
            reject();
        }
    })
} 

const server = http.createServer((request, response) => {
    const { method, url } = request;
    console.log(method, url);

    if (url.includes("favicon.ico")) {
        console.log("Favicon");
        return response.end();
    }
    const file = fs.readFileSync("./app" + url + "/page.html", (err, data) => {
        if (err) {
            console.log("Error occured");
            response.statusCode = 404;
            response.write("<html>");
            response.write("<head>");
            response.write("<title>404 Not found!</title>");
            response.write("</head>");
            response.write("<body><h1>Requested resource not found</h1><a href='/'>Go to home</a></body>");
            response.write("</html>");
            return response.end();
        };
    });
    response.write(file.toString())
    return response.end()


}).listen(PORT)

console.log(`Listening on port ${PORT}`);
console.log(`http://localhost:${PORT}`);