/* 
图片上传是Web开发中常用的功能
使用第三方模块 multer 来实现
*/
const Express = require('express')
const Multer = require('multer')
const Path = require('path')

const app = Express()

app.use(Express.static(Path.join(__dirname,'public')))
app.use(Express.static(Path.join(__dirname,'sources')))
// 最简单的方式来使用 multer
// 设置图片的存储目录
let uploadPath = Path.join(__dirname,'sources/images/')
// 创建multer 存储文件对象
// 设置存储路径是使用了 multer的参数 dest的值来自定义目录
const multer = Multer({dest:uploadPath})

// 单图上传
// single(name) 表示 单张图片的上传 
// 其中 name 是要跟传递标识要保持一致
// 目的是 为了能确保 在传递 图片时 键值的对应
// 此name 表示由前端页面中的表单指定
let single_file = multer.single('logo')

// 需要在指定的POST请求处理中 设置 响应的上传属性 single_file
app.post('/upload',single_file,(req,res)=>{
    console.log(req.file)
    /* file属性就是图片上传对应图片
    fieldname: Field name 由表单指定
    originalname: 用户计算机上的文件名称
    encoding: 文件编码
    mimetype: 文件的类型
    size:文件的大小（字节单位）
    destination:保存的路径
    filename:保存在destination中的文件名
    path:已上传文件的完整路径
    buffer：一个存放了整个文件的Buffer
    */
    res.send('上传成功')
})

/* 指定路径存储和指定文件名称 */
// 判断有没有要存储的目录 没有创建

// 要先 配置 要存储的目录和名称
let st = Multer.diskStorage({
    destination: uploadPath,
    filename:(req,file,cb)=>{
        cb(null,'1.jpg')
    }
})
let multer2 = Multer({storage:st})
let single2 = multer2.single('logo')

app.post('/upload2',single2,(req,res)=>{

    res.send(req.file.path)
})

// ============================================================
/* 上传多张图片 */
/* 1. */
let st2 = Multer.diskStorage({
    destination: (req,file,cb)=>{

        console.log(file)
        cb(null,Path.join(__dirname,'sources/images/'))
    },
    filename: (req,file,cb)=>{
        cb(null, file.originalname)
    }
})
let multer3 = Multer({storage:st2})
let files = multer3.array('logos',3)

// let filess = multer3.fields([
//     {name:"logo1",maxCount:2},
//     {name:"logo",maxCount:1}
// ])


app.post('/uploads',files,(req,res)=>{
    res.send(req.files)
})


app.listen(9001)
