<template>
  <div>
    <h1>B</h1>
    <h2>
      {{ this.$store.state.userName }}
    </h2>
    <button @click="changeCity()">最喜欢的城市</button>
    <h3>{{ this.$store.state.city }}</h3>
  </div>
</template>

<script>
export default {
  name: 'B',
  methods: {
      changeCity(){
        //  this.$store.dispatch('emitCity','大三门峡') 
        this.$store.commit('citys','大三门峡') 
      }
  },
}
</script>

<style>
  
</style>