/* 主页路由 */
const Express = require('express')
// 引入子路由
const goodsRouter = require('./goods/goods')
// 引入router模块 并实例化路由对象
const router = Express.Router()

router.use('/goods', goodsRouter)

router.get('/',(req, res)=>{
    res.send('<h1>Home</h1>')
})


module.exports = router