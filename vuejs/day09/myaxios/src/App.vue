<template>
  <div id="app">
    <router-view/>
		<button @click="getJson()">请求json数据</button>
		<button @click="es6Then()">Promise方式进行异步编程</button>
		<button @click="xhrPromise()">用户登录</button>
		<button @click="nodeLogin()">访问Node服务器</button>
		<button @click="es6Promise()">Promise方式访问Node服务器</button>
		<button @click="testPromise()">测试then的连续性</button>
		<promise-c></promise-c>
  </div>
</template>

<script>
let url_string = "http://localhost:8080/static/json/moves.json"
let login_string = "http://localhost:8080/static/json/login.json"
import axios from 'axios'
import PromiseC from '@/components/PromiseC'
export default {
  name: 'App',
	components:{
		'promise-c': PromiseC
	},
	methods:{
		testPromise(){
			let task = new Promise(function(resolve,reject){
				console.log('任务启动')
				setTimeout(function(){
					console.log('返回处理结果')
					reject('111111111')
				},2000)
			})
			task.then(function(res){
				console.log(res)
				return '2'
			},function(error){
				console.log(error)
				throw error
				// return error
			}).then(function(res){
				console.log('*****2*****')
				console.log(res)
				console.log('end')
				return '3'
			}).catch(function(error){
				console.log(error)
			})
		},
		es6Promise(){
			// Promise 站在任务调度
			// 
			let task = new Promise(function(resolve,reject){
				// 要做的事情 任务
				let url = "http://localhost:10000/v2/login"
				let xhr = new XMLHttpRequest()
				xhr.open('GET',url)
				xhr.send()
				xhr.onreadystatechange = function(){
					if(4 == xhr.readyState && 200 == xhr.status){
						let obj = JSON.parse(xhr.responseText)
						if(!obj.error){
							// 正确的处理结果
							// Promise 规定正确的处理是同过 resolve进行 回调
							resolve(obj)
						}else{
							console.log('登录失败')
							// reject 失败时需要的回调
							reject(obj)
						}
					}
				}
			})
			// then()方法 来处理 Promise 对象 的异步处理结果
			task.then(function(res){
				console.log(res)
			})
		},
		getJson(){
			axios.get('http://localhost:10000/v2/home').then(function(res){
				// console.log(res)
				// console.log(res.data.subjects)
				res.data.subjects.forEach(function(item){
					console.log(item.title)
				})
			})
		},
		es6Then(){
			// 异步编程
			// 同一时间可以处理多个事件的操作
			// 线程操作
			// 主线程 子线程
			// JS 单线程
			// 通过调度任务来实现多线程
			// ES6 引入 一个新类 promise 类 专门用来做异步编程
			console.log('before')
			let task1 = new Promise(function(resolve,reject){
				if(false){
					resolve('成功')
				}else{
					reject('失败')
				}
			})
			console.log(typeof task1)
			task1.then(function(msg){
				console.log("1:",msg)
			})
		
			console.log('after')
		},
		xhrPromise(){
			// 实际的工作环境中有这种情况 第二个请求的请求条件是第一个请求的结果
			let xhr = new XMLHttpRequest()
			xhr.open('GET',login_string)
			xhr.send()
			xhr.onreadystatechange = function(){
				if(4==xhr.readyState && 200 == xhr.status){
					let obj = JSON.parse(xhr.responseText)
					if(obj){
						if(!obj.error){
							console.log(obj.msg)
							console.log(obj.home_url)
							// 再次发送请求
						}else{
							console.log('登录失败')
						}
					}
				}
			}
			
			let xhr2 = new XMLHttpRequest()
			xhr2.open('GET',url_string)
			xhr2.send()
			xhr2.onreadystatechange = function(){
				if(4 == xhr2.readyState && 200 == xhr2.status){
					let obj2 = JSON.parse(xhr2.responseText)
					if(obj2.subjects){
						obj2.subjects.forEach(function(item){
							console.log(item.title)
						})
					}
				}
			}
			
		},
		nodeLogin(){
			let url = "http://localhost:10000/v2/login"
			console.error('**********1 start***************')
			let xhr = new XMLHttpRequest()
			xhr.open('GET',url)
			xhr.send()
			xhr.onreadystatechange = function(){
				if(4 == xhr.readyState && 200 == xhr.status){
					console.log(xhr.responseText)
					console.error('**********2***************')
					let xhr2 = new XMLHttpRequest()
					xhr2.open('GET',"http://localhost:10000"+JSON.parse(xhr.responseText).home_url)
					xhr2.send()
					xhr2.onreadystatechange = function(){
						if(4 == xhr2.readyState && 200 == xhr2.status){
							console.log(xhr2.responseText)
							console.error('**********4***************')
						}
					}
				}
			}
			
			url = "http://localhost:10000/v2/home"
			console.error('**********3***************')
			
			
			console.error('**********5 end***************')
		}
		//1 3 5 2 4 // 1 3 2 5 4 
		//1 3 5 2 4 
	}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
