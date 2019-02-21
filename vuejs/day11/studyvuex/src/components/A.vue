<template>
  <div>
    <h1>A Vuex就是用来实现数据共享</h1>
    <h2>
      {{ this.$store.state.userName }}
    </h2>
    <h3>{{ this.$store.state.city }}</h3>
  </div>
</template>

<script>
export default {
  name: 'A'
}
</script>

<style>
  
</style>