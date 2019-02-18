<template>
	<div>
		{{ msg }}
		<ul>
			<li v-for="(item,index) in studs" :key="index">
				<!-- <span>{{ item.sname }}</span> -->
				<stu :stuinfo="msg" :item="item"></stu>
			</li>
		</ul>
		
	</div>
</template>

<script>
import Stu from '@/components/Stu'
export default {
	name:'ItemInfo',
	components:{
		'stu': Stu
	},
	props:['msg','studs']
}
</script>

<style>
</style>
