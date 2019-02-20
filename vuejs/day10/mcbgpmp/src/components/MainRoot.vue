<template>
  <div class="mc-main">
    <!-- 页面的内容切换2种方式
    1.使用v-if v-show 指令来切换
    2.使用 router 切换
     -->
    <!-- 2个界面显示
    1.登录界面
    2.主界面
     -->
    <!-- <button @click="jump()">切换</button> -->
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: "MainRoot",
    data() {
      return {
        isLogin: false
      }
    },
    mounted() {
      if (!this.isLogin) {
        this.$router.push("login") 
      }else{
        this.$router.push("home")
      }
      
    },
    methods: {
      jump(){
        console.log(this.$router)
        // this.$router.push("home")
        this.$router.push("login")
      }
    }
  }
</script>

<style>
html,body {
  margin: 0;
  padding: 0;
  height: 100%;
}
/* #app {
  height: 100%;
} */
.mc-main{
  height: 100%;
}
</style>
