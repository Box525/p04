const Express = require('express')
const BodyParser = require('body-parser')
const Multer = require('multer')
const Path = require('path')

// 自定义模块
const oa = require('./mod/oauth/oauth')

const app = Express()
// 开放文件夹
app.use(Express.static(Path.join(__dirname,'public')))
app.use(Express.static(Path.join(__dirname, 'sources')))
app.use(Express.static(Path.join(__dirname,'sources/images')))

// 设置解析 form data 表单数据 针对 POST请求
app.use(BodyParser.urlencoded({extended:false}))
app.use(BodyParser.json())

// 设置存储路径
let st = Multer.diskStorage({
    destination:(req,file,cb)=>{
        cb(null, Path.join(__dirname,'sources/images'))
    },
    filename: (req,file,cb)=>{
        cb(null,file.originalname)
    }
})

let multer = Multer({stroage: st})

app.get('/',(req,res)=>{
    res.redirect('index.html')
})


function cb(res,data) {
    res.send(data)
}


//TODO: 注册
app.post('/register',(req,res)=>{
    // 1.判断用户是否合法 2.存储有效文件中
    // oa.oauth({uname:'tom'},(data)=>{
    //     console.log('index.js,' , data)
    //     res.send(data)
    // })
    // oa.oauth({uname:'tom'},cb)
    oa.oauth({uname:'tom'},function (data){
        res.send(data)
    })
    console.log('eeeeeennnnnnnddddd')
    // res.send(req.body)
})


app.listen(10086)



