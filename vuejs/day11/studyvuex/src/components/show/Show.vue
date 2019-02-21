<template>
  <div class="show">
    <router-link :to="{name,params:{id}}"></router-link>
    <h1>内容展示</h1>
    <!-- 画布 -->
    <component :is="showView"></component>
  </div>
</template>

<script>
import A from '@/components/A'
import B from '@/components/B'
export default {
  name: 'Show',
  data() {
      return {
          showView: B,
          name: 'datas',
          id:'11'
      }
  },
  watch: {
      '$route'(to,from){
        //   console.log(to,from)
          console.log(this.$route.params.id)
        //   switch(this.$route.query.id){
        //                 case '1':this.currentView = home;break;
        //                 case '2':this.currentView = list;break;
        //                 case '3':this.currentView = detail;break;
        //                 default:this.currentView = home;
        //             }
      }
  },
}
</script>

<style>
.show {
    border: 1px solid red;
}
</style>