const Express = require('express')
const BodyParser = require('body-parser')
const Multer = require('multer')
const Path = require('path')

// 引入跨域 CORS 包/模块
const Cors = require('cors')

// 自定义模块
const oa = require('./mod/oauth/oauth')

const app = Express()
// 开放文件夹
app.use(Express.static(Path.join(__dirname ,'public')))
app.use(Express.static(Path.join(__dirname, 'sources')))
app.use(Express.static(Path.join(__dirname,'sources/images')))

// 设置解析 form data 表单数据 针对 POST请求
app.use(BodyParser.urlencoded({extended:false}))
app.use(BodyParser.json())

// app.use(Cors())
// app.use(Cors({
	// origin: ['http://127.0.0.1:8080'],
	// methods: ['GET', 'POST'],
	// alloweHeaders: ['Conten-Type', 'Authorization']
// }))

app.get('/',(req,res)=>{
	res.redirect('index.html')
})

app.get('/json',Cors({
	origin: ['http://127.0.0.1:8080'],
	methods: ['GET', 'POST'],
	alloweHeaders: ['Conten-Type', 'Authorization']
}),(req,res)=>{
	res.send(JSON.stringify({
		err:true,
		code:'10086'
	}))
})
app.get('/json2', (req, res) => {
	res.send(JSON.stringify({
		err: true,
		code: '10086'
	}))
})


app.get('/favicon.ico',(req,res)=>{
	res.send('')
})


//TODO: 注册
app.post('/register',(req,res)=>{
	// 1.判断用户是否合法 2.存储有效文件中
	// oa.oauth({uname:'tom'},(data)=>{
	//     console.log('index.js,' , data)
	//     res.send(data)
	// })
	// oa.oauth({uname:'tom'},cb)
	let user = req.body
	oa.oauth(user,function (err,result){
		// eslint-disable-next-line no-console
		console.log(err,result)
		if (err) {
			let obj = {
				code: '1001',
				err: true
			}
			res.send(JSON.stringify(obj))
		}
		if (!result) { //
            // 没有找到这个用户 表示 这是新用户
            user['dirname'] = user.uname
			oa.add(user,function (err,result) {
				if (err) {
					let obj = {
						code: '50001',//系统错误
						err: true
					}
					res.send(JSON.stringify(obj))
				}
				if (result) {
					let obj = {
						code: '',
						err: false,
						msg: result
					}
					res.send(JSON.stringify(obj))
				}else{
					let obj = {
						code: '',
						err: true,
						msg: '注册失败'
					}
					res.send(JSON.stringify(obj))
				}
			})
		}else{
			// 有
			let obj = {
				code: '2001',//2001 表示用户已存在
				err: true
			}
			res.send(JSON.stringify(obj))
		}
	})
	// res.send(req.body)
})

app.post('/login',(req ,res)=>{
	// 验证通过不了 就 返回 json
	// 验证通过则直接跳转 主页
	// res.redirect('home.html')
    
	res.send(JSON.stringify({
		err: false,
		msg: '登录成功'
	}))
})

app.get('/user',(req,res)=>{
	// 用户验证
	let user = req.query
    
	res.send(JSON.stringify({
		err: false,
		msg: '用户合法'
	}))
})

app.get('/user/dlist',(req,res)=>{
    let user = req.query
    // 
    console.log(user)
	// 用户验证
	oa.oauth(user,function (err,result) {
		if (err) {
			res.send(JSON.stringify({
				err: true,
				msg: '验证失败'
			}))
		}
		if(result){
            // 用户存在 便是验证通过
            user['dirname'] = user.uname
			oa.files(user,function (err,files2) {
				if (err) {
					res.send(JSON.stringify({
						err: true,
						msg: '目录不存在'
					}))
                }
                // 过滤 文件夹 前面有. 的情况
                let flist = []
                for(let i = 0; i < files2.length ;i++){
                    let item = files2[i]
                    if (item[0] != '.') {
                        flist.push(item)
                    }
                }

                files2 = flist

                res.send(JSON.stringify({
                    err: false,
                    files: files2
                }))
			})

		}
	})
	// 


})

app.get('/user/plist',(req,res)=>{
    // 获取前端请求 数据
    let user = req.query
    oa.oauth(user,function (err,result) {
        if (err) {
            res.send(JSON.stringify({
                err: true,
                msg: '验证失败'
            }))
        }
        if (result) {
            user['dirname'] = user.uname + '/' + user.dname
            oa.files(user,function (err,files) {
                if (err) {
                    res.send(JSON.stringify({
                        err: true,
                        msg: '目录不存在'
                    }))
                }
                res.send(JSON.stringify({
                    err: false,
                    files: files
                }))
            })
        }
    })

})

app.post('/user/pic/add',(req,res)=>{
	res.send('hello')
})

// 设置存储路径 
let st = Multer.diskStorage({
	destination: (req, file, cb) => {
		console.log(file)
		cb(null, Path.join(__dirname, 'sources/images/'))
	},
	filename: (req, file, cb) => {
		cb(null, file.originalname)
	}
})

let multer = Multer({
	storage: st
})

let single2 = multer.single('logo')
app.post('/user/add/pic',single2,(req,res)=>{
	console.log(req)
	res.send(JSON.stringify({
		code: '',
		msg: '上传成功',
		data :{
			src: req.file.path
		}
	}))
})

app.listen(10086)
