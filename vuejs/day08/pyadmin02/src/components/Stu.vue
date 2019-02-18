<template>
	<div class="stu">
		{{ stuinfo }}:{{ item.sname }}
	</div>
</template>

<script>
export default {
	name:'Stu',
	props:['stuinfo','item']
}
</script>

<style>
	.stu{
		border: 1px solid springgreen;
	}
</style>
