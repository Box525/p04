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
    }
  },
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
