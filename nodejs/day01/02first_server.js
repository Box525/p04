var http = require('http')
http.createServer(function (req,res) {
    res.write('<head><meta charset="utf-8"></head>')
    res.write('这是一个中文')
    res.end('这是一个写的结束')
}).listen(8080)
console.log('http is running, port is 8080')