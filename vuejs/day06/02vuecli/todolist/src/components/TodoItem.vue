<template>
	<li>
		<span>{{ content }}</span>
		<button @click="delOne()">删除</button>
	</li>
</template>

<script>
export default {
	name:'TodoItem',
	props:['content'],
	methods: {
		delOne(){
			console.log('删除')
			this.$emit('cb',1)
		}
	}
}
</script>

<style>
</style>
