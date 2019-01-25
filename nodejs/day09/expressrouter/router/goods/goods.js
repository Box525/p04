/* 商品路由 */
const Express = require('express')
// 引入router模块 并实例化路由对象
const router = Express.Router()

router.get('/', (req, res) => {
    res.send('<h1>商品</h1>')
})


module.exports = router