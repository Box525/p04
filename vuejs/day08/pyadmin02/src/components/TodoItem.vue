<template>
	<li>
		<span>{{ item.cname }}</span>
		<button @click="show(index,item.cname)">查看</button>
	</li>
</template>

<script>
	export default{
		name: 'TodoItem',
		props:['item','index'],
		methods:{
			show(id,cname){
				this.$emit('cb',id,cname)
			}
		}
	}
</script>

<style>
</style>
