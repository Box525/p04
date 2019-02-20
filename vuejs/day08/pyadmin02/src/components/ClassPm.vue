<template>
	<div>
		<h1>班级学生列表</h1>
		{{ cid }}
	</div>
</template>

<script>
export default {
	name: "ClassPm",
	computed:{
		cid(){
			console.log(this.$route.params)
			return this.$route.params.cid
		}
	}
}
</script>

<style>
</style>
