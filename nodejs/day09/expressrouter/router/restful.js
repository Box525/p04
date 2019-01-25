/* 
REST 是约束和原则 是一种设计模式
RESTful 使用REST实现的应用 是一种开发模式

REST ：表现层状态转移

白话：就是用URL定位资源，用HTTP描述操作

URL定位资源，用HTTP动词（GET、POST、PUT、DELETE）描述操作

// 
URL: http://www.photo.com/user/pic 
用户图片管理的操作
对于图片的操作 add 、 delete 、 edit 、show
不满足REST风格的做法：
要实现4个接口
/user/pic/show: 展示图片 GET
/user/pic/add: 增加一张图片 POST
/user/pic/edit : 更新一张图片 POST
/user/pic/delete: 删除一张图片 GET/POST

REST风格的做法
/user/pic
GET: 查看操作
POST: 增加操作
PUT: 更新
DELET: 删除

参考文献:
https: //blog.csdn.net/caishu1995/article/details/86151044
https: //blog.csdn.net/chenxiaochan/article/details/73716617
https: //blog.csdn.net/qq_21383435/article/details/80032375
http: //www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html
*/

const Express = require('express')
const router = Express.Router()

// pic

router.get('/',(req, res)=>{
    res.send('<h1>这是查看指定图片</h1>')
})

router.post('/',(req, res)=>{
    res.send('<h1>这是增加指定图片</h1>')
})

router.put('/',(req, res)=>{
    res.send('<h1>这是更新指定图片</h1>')
})

router.delete('/', (req, res) => {
    res.send('<h1>这是删除指定图片</h1>')
})

module.exports = router