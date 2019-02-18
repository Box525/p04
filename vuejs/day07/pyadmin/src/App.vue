<template>
	<div id="app">
		<el-container>
			<el-header>
				<py-header :message="msg"></py-header>
			</el-header>
			<el-container>
				<el-aside width="200px">
					<h1>折叠菜单</h1>
					<!-- <el-menu :default-active="'2'" @select="handleSelect">
						<el-menu-item index="1">首页</el-menu-item>
						<el-menu-item index="2">首页2</el-menu-item>
						<el-submenu index="3">
							<template slot="title">
								这是标题1
							</template>
							<el-menu-item index="3-1">首页</el-menu-item>
						</el-submenu>
					</el-menu> -->
					<el-menu @select="handleSelect">
						<el-submenu v-for="(menu,index) in menus.menus" :index="index+1+''" :key="index">
							<template slot="title">
								<h3>{{ menu.menuname }}</h3>
							</template>
							
						</el-submenu>
					</el-menu>
				</el-aside>
				<el-main>Main</el-main>
			</el-container>
		</el-container>
	</div>
</template>

<script>
	var json = {
		"menus":[
			{
				"menuname":"一班",
				"groups":[
					{
						"groupname":"第一组"
					},
					{
						"groupname":"第二组"
					},
					{
						"groupname":"第三组"
					}
				]
			},
			{
				"menuname":"二班",
				"groups":[
					{
						"groupname":"第一组"
					},
					{
						"groupname":"第二组"
					},
					{
						"groupname":"第三组"
					},
					{
						"groupname":"第四组"
					}
				]
			}
		]
	}
	import PyHeader from '@/components/PyHeader'
	export default {
		name: 'App',
		components:{
			'py-header': PyHeader
		},
		data(){
			return {
				menus: json,
				msg: '这是组件传值'
			}
		},
		methods:{
			handleSelect(key,keyPath){
				console.log(key,keyPath)
			}
		}
	}
</script>

<style>
	html,body {
		margin: 0;
		padding: 0;
	}
	/* * {
		border: 1px red solid;
	} */
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		/* text-align: center; */
		color: #2c3e50;
	}
	
	#app .el-header {
		background-color: #2C3E50;
	}
</style>
