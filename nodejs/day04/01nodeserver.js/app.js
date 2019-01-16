// 这是服务器端应用程序 提供了Web应用服务
// 作用是为 客户端访问提供 数据服务

// 1.引入 http 服务模块
const http = require('http')
// 2.引入url 模块 对 URL 进行解析
const url = require('url')

// 3.初始化 应用服务
let server = http.createServer((req,res)=>{
    res.writeHead(200,{
        'Content-Type':'text/html;charset=utf-8'
    })
    // home about login register
    // 5.获取 请求中的url 的 path 目录
    let pathname = url.parse(req.url).pathname
    // 6.路径处理 (路由)
    showPage(pathname,res)
    res.end()
})

// 4.启动应用服务
server.listen(9001)


// 7.实现 对 路径的处理（数据的处理）
function showPage(pn,res) {
    switch (pn) {
        case '/favicon.ico':
            break;
        case '/home/':
            res.write('<h1>首页abc</h1>')
            break;
        case '/about/':
            res.write('<h1>关于</h1>')
            break;
        case '/login/':
            let html_content = `
                <h1>欢迎登录</h1>
                <form action='/register/'>
                    <input type='text' name='uname'>
                    <input type='submit' value='注册'>
                </form>
            `
            res.write(html_content)
            break;
        case '/register/':
            // res.write('<h1>注册</h1>')
            // 写JSON数据
            // 1.键值对  2.最外层{ } 3.值的类型：6种
            let json_data = {
                uname: 'Tom',
                uage: 18,
                ufriends:[
                    'Jack','Rose'
                ],
                umarry: false,
                uhouse: null,
                ulike: {
                    like: 'play'
                },
                usex: 'm'
            }
            let json_string = JSON.stringify(json_data)
            res.write(json_string)
            break;
        default:
            res.write('<h1>404</h1>')
            break;
    }


}

/* 服务器端原理：
使用Node.js作为后端的开发项目，客户访问过程：
客户端发起请求--> node.js服务器接收到请求并解析、运算---》
返回结果对客户端完成响应
*/
