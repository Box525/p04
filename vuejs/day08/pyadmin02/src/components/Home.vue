<template>
	<div>
		<h1>主页</h1>
		<router-link to="/home/product">商品</router-link>
		<router-view></router-view>
	</div>
</template>

<script>
export default {
	name: "Home"
}
</script>

<style>
</style>
