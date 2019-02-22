<template>
  <div id="app">
    <button @click="change()">切换用户名</button>
    <!-- <a-com></a-com>
    <b-com></b-com> -->
    <menus></menus>
    <show></show>
  </div>
</template>

<script>
import A from '@/components/A'
import B from '@/components/B'
import Menus from '@/components/navs/Menus'
import Show from '@/components/show/Show'
// import { aCity , bCity , dd, msg } from '@/assets/js/moduleA.js'
import * as obj from '@/assets/js/moduleA.js'
// import name from '@/assets/js/moduleB.js'
import Pp from '@/assets/js/moduleB.js'
export default {
  name: 'App',
  components: {
    'a-com': A,
    'b-com': B,
    'menus': Menus,
    'show': Show
  },
  methods: {
    change(){
      // dispatch('派发给哪一个action','要修改的内容')
      // this.$store.dispatch('newUserName','统一中国')
      this.$store.commit('newUserName','统一中国')
      let city2 = city
      console.log('城市：',city2) 
    }
  },
  mounted() {
    let city2 = obj.aCity
    console.log('城市：',city2) 
    city2 = obj.bCity
    console.log('城市：',city2)
    console.log(obj.dd)
    obj.msg('今天是2019年2月22')
    // console.log(name.name2)
    console.log(Pp.name)
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
  /* margin-top: 60px; */
}
</style>
