/* 用户路由 */
const Express = require('express')
// 引入router模块 并实例化路由对象
const router = Express.Router()

router.get('/', (req, res) => {
    res.send('<h1>用户</h1>')
})

router.get('/register', (req, res) => {
    res.send('<h1>注册</h1>')
})

router.get('/login', (req, res) => {
    res.send('<h1>登录</h1>')
})

module.exports = router