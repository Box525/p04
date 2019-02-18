<template>
	<div class="hello">
		<h1>TodoList 组件</h1>
		<ul>
			<todo-item v-for="(item,index) in lists" :key="index" :content="item" :index="index" @cb="dd"></todo-item>
		</ul>
	</div>
</template>

<script>
import TodoItem from '@/components/TodoItem'
export default {
	name: 'TodoList',
	components:{
		'todo-item': TodoItem
	},
	props:['lists','msg'],
	methods:{
		dd(index){
			console.log('dd:',index)
			this.$emit('delete',index)
		}
	}
}
</script>

<style>
</style>
