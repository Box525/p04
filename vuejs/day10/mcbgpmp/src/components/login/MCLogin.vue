<template>
  <el-container>
    <el-main>
      <h1>主内容</h1>
    </el-main>
    <el-aside width="300px">
      <h1>侧边栏</h1>
    </el-aside>
  </el-container>
</template>

<script>
export default {
  name: 'MCLogin'
}
</script>

<style scoped>
.el-container {
  background-color: #666;
  height: 100%;
  min-width: 800px;
  min-height: 600px;
}
</style>
