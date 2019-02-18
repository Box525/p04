<template>
	<li class="hello">
		<span>{{ content }}</span>
		<button @click="delOne(index)">删除</button>
	</li>
</template>

<script>
export default {
	name:'TodoItem',
	props:['content','index'],
	methods: {
		delOne(id){
			console.log('删除')
			this.$emit('cb',id)
		}
	}
}
</script>

<!-- scoped 表示这是一个局部样式，不写则表示是组件的全局样式会被共用 -->
<style scoped>
.hello{
	border: 2px solid #42B983;
}
</style>
