const Express = require('express')
const Path = require('path')
const homePage = require('./router/home')
const userRouter = require('./router/user')
const picRouter = require('./router/restful')

const app = Express()

/* 路由
node.js 路由是指对浏览器地址的一种解析
URL
通过路由可以实现不同模块的调用，从而实现不同的页面和功能

express 中的路由
Router 的模块来实现路由功能
router模块 目的是：中间件和路由的分离
*/

app.use(Express.static(Path.join(__dirname,'public')))

app.use('/home',homePage)
app.use('/user', userRouter)
app.use('/pic', picRouter)


app.listen(10086,()=>{
    console.log('10086 server is running......')
})