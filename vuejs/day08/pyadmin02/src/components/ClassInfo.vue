<template>
	<div>
		<!-- 左侧班级列表 -->
		<ul>
			<li v-for="(item,index) in classes" :key="index">
				<router-link :to="{name:'cid',params:{cid:item.cid}}">{{ item.cname }}</router-link>
			</li>
		</ul>
		<div>
			<router-view></router-view>
		</div>
	</div>
</template>

<script>
var dd = {
	cc: [
		{cname:'1班',cid:'001'},
		{cname:'2班',cid:'002'},
		{cname:'3班',cid:'003'},
		{cname:'4班',cid:'004'},
		{cname:'5班',cid:'005'},
		{cname:'6班',cid:'006'}
	]
}
	
export default{
	name: 'ClassInfo',
	data(){
		return {
			classes:dd.cc
		}
	}
}
</script>

<style>
</style>
