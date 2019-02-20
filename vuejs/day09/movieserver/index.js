const express = require('express')
const fs = require('fs')
const cors = require('cors')

const app = express()
var corsOptions = {
  origin: 'http://localhost:8080', //只有百度可以访问
  optionsSuccessStatus: 200 
}

app.get('/v2/login',cors(corsOptions),(req,res)=>{
	let json = {
		error: false,
		msg: '登录成功',
		'home_url': '/v2/home'
	}
	res.send(JSON.stringify(json))
})

app.get('/v2/home',cors(corsOptions),(req,res)=>{
	// fs.open('./api/moves.json')
	fs.readFile('./api/moves.json',(err,fd)=>{
		if(err){
			let json = {
				error: true,
				msg: '文件读取失败，请联系管理员'
			}
			res.send(JSON.stringify(json))
		}
		
		res.send(fd.toString())
	})
})





app.listen(10000)