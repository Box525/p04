<template>
	<div>
		<p>{{message}}</p>
		<el-row :gutter="20">
			<el-col :span="6">
				左
			</el-col>
			<el-col :span="6" :offset="12">
				右
			</el-col>
		</el-row>
	</div>
</template>

<script>
export default {
	name: 'PyHeader',
	props: ['message']
}
</script>

<style scoped>
	.row{
		border: 1px solid red;
	}
	.el-col {
		border: 1px solid red;
	}
</style>
