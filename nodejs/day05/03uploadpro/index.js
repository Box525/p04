const Express = require('express')
const BodyParser = require('body-parser')
const Multer = require('multer')
const Path = require('path')

const app = Express()

app.use(Express.static(Path.join(__dirname,'public')))
app.use(BodyParser.urlencoded({extended:false}))

let uploadDir = Path.join(__dirname,'images/')
let multer = Multer({dest:uploadDir})

let single = multer.single('logo')

app.post('/upload',single,(req,res)=>{
    console.log(req.body)

    res.send(req.body)
})

app.listen(9999)


/* 作业要求
功能：存储用户的图片
1.指定的用户，图片要存储到对应目录下，目录的名称是用户名，
用户名使用手机号最为用户名
2.用户目录下 使用时间格式 进行 目录分类 例如 20190117
3.对应时间上传的文件，存储到对应的时间目录下
4.文件的名称使用毫秒+文件后缀 为新的文件名称，不能修改原有文件后缀

*/
