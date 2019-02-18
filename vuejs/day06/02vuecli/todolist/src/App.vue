<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
		<input type="text" v-model="msg">
		<p>{{ msg }}</p>
		<button type="primary" @click="send()">提交</button>
		<!-- 3.使用组件 -->
		<todo-list :lists="lists" :msg="msg" @delete="handleDel"></todo-list>
  </div>
</template>

<script>
// 1.导入组件
import TodoList from "@/components/TodoList"
export default {
  name: 'App',
	components:{
		'todo-list':TodoList
	},//2.声明组件
	data(){
		return {
			msg: '今天是2019年2月14日，白色情人节',
			lists: []
		}
	},
	methods:{
		send(){
			// console.log(this)
			this.lists.push(this.msg)
		},
		handleDel(index){
			console.log('app:',index)
			this.lists.splice(index,1)
		}
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
  margin-top: 0px;
}
</style>
