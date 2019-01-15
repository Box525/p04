/* 
GET 方法

在开发中，很多场景中
服务器都需要和用户的浏览器打交道，比如 表单提交
表单提交一般只有2种方式 GET/POST
如果获取 GET 请求内容
因为 GET请求直接被嵌入在路径中，
URL是完整的请求路径，包含了？号后面的部分
服务器需要手动解析后面的内容方能拿到GET的参数

Nodejs 中使用 url 模块 中的 parse来 解析

*/

const http = require('http')
const url = require('url')

http.createServer((req,res)=>{
    res.writeHead(200,{
        'Content-Type':'text/html;charset=utf-8'
    })

    let gets = url.parse(req.url,true)
    console.log(gets.query)

    res.end()
}).listen(9000)

