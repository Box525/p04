<template>
	<div id="app">
		<div>
			<div>
				<!-- 左边 -->
				<todo-item v-for="(item,index) in datas.class" :key="index" :item="item" :index="index" @cb="handleShow"></todo-item>
			</div>
			<div>
				<!-- 右边 -->
				<!-- {{ msg }} -->
				<item-info :msg="msg" :studs="stu"></item-info>
			</div>
		</div>
		<div>
			<div>
				<!-- 导航 -->
				<!-- <router-link to="/homehome">主页</router-link> -->
				<router-link :to="{name: ''}">主页</router-link>
				<router-link to="/class">班级列表</router-link>
			</div>
			<div>
				<!-- 展示区域 -->
				<router-view />
			</div>
		</div>
		
	</div>
</template>

<script>
	var dd = {
		'class':[
			{"cname":"1班","studs":[{"sname":"Tom"}]},
			{"cname":"2班","studs":[{"sname":"Tom2"}]},
			{"cname":"3班","studs":[{"sname":"Tom3"}]}
		]
	}
	import TodoItem from '@/components/TodoItem'
	import ItemInfo from '@/components/ItemInfo'
	export default {
		name: 'App',
		components:{
			'todo-item':TodoItem,
			'item-info':ItemInfo
		},
		data() {
			return {
				datas: dd,
				msg:'',
				stu:[]
			}
		},
		methods:{
			handleShow(index,cname){
				console.log(index,cname),
				this.msg = cname
				this.stu = this.datas.class[index].studs
			}
		}
	}
</script>

<style>
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		/* text-align: center; */
		color: #2c3e50;
	}
</style>
