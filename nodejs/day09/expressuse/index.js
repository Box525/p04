const Express = require('express')

const app = Express()
// Express 是一个自身功能极简,
// 完全是由路由和中间件构成一个的 web 开发框架:
// 从本质上来说,一个 Express 应用就是在调用各种中间件。

/* 
在Express 内部，有一个函数 数组，暂时把这个数据称为 tasks
每一个请求 express 内部都会依次执行这个数组中的函数（有个前提，
每一个函数必须满足一定的条件才能 被执行）
在这个函数数组中，每一个函数的签名都应该满足下面的方式
function(req,res){
    // 请求和响应处理
}
但是 真正的函数 是长这个样子的
function (req, res, next) {
    // 请求和响应处理
}
next 是指下一个函数
*/


app.use('/home',function (req, res, next) {
    console.log('这是11')
    next()
    console.log('这是12')
})



app.get('/',(req, res, next)=>{
    // res.send('<h1>这是首页1</h1>')
    console.log('这是1号')
    next()
    // res.send('<h1>这是首页3</h1>')
    console.log('<h1>这是首页3</h1>')
    console.log('这是2号')
})
app.get('/123', (req, res, next) => {
    // res.send('<h1>这是首页1</h1>')
    console.log('这是3号')
    next()
    console.log('这是4号')
})
app.get('/', (req, res, next) => {
    // res.send('<h1>这是首页1</h1>')
    console.log('这是5号')
    next()
    console.log('这是6号')
})

app.get('/', (req, res) => {
    console.log('这是7号')
    res.send('<h1>这是首页2</h1>')
    console.log('这是8号')
})

app.post('/', (req, res) => {
    res.send('<h1>这是首页</h1>')
})

app.get('/json',(req, res)=>{
    res.send(JSON.stringify({
        msg: '这是json数据响应'
    }))
})




app.listen(10086,function () {
    console.log('10086 Server is running.......')
})