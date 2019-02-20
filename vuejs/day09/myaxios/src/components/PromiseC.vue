<template>
	<div>
		<button @click="task()">开发模式中的真实使用</button>
	</div>
</template>

<script>
/* A请求 B请求
B请求的请求参数 需要A请求之后返回结果
耗时的任务都必须使用 异步任务
 */
// A任务
function aTask(dd){
	let task = new Promise(function(resolve,reject){
		// 耗时任务 模拟
		console.log('A任务开始启动')
		setTimeout(function(){
			console.log('A任务结束')
			resolve('这是a任务返回的结果')
		},2000)
	})
	
	return task
}

// B任务
function bTask(dd){
	console.log(dd)
	let task = new Promise(function(resolve,reject){
		// 耗时任务 模拟
		console.log('B 任务开始')
		setTimeout(function(){
			resolve('这是B任务返回的结果')
			console.log('B 任务结束')
		},3000)
	})
	return task
}

export default {
	name: 'PromiseC',
	methods:{
		task(){
			// 工作中的使用方式
			aTask().then(bTask).then(function(res){
				console.log(res)
				console.log('总任务结束')
			})
		}
	}
}
</script>

<style>
</style>
