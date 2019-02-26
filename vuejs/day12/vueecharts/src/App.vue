<template>
  <div id="app">
    <div id="my_cavans" style="width:500px;height:300px;border:1px solid red;"></div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  mounted() {
    this.drawView()
  },
  methods: {
    drawView(){
      // 初始化 echarts的绘制对象
      let my_echarts = this.$echarts.init(document.getElementById('my_cavans'))
      let option = {
        title: {
          text: '2月天气'
        },
        xAxis: {
          data:['2.1','2.2','2.3']
        },
        yAxis: [
          {
            type: 'value',
            name: '温度',
            max: 50,
            min: -20,
            interval: 10,
            axisLabel:{
              formatter:'{value}°C'
            }
          },
          {
            type: 'value',
            name: 'PM2.5值',
            max: 300,
            min: 0,
            interval: 40,
            axisLabel:{
              formatter:'{value}PM'
            }
          }
        ],
        series:[
          {
            type: 'line',
            data:[-5,5,20]
          },
          {
            type: 'line',
            data:[150,50,300]
          }
        ]
      }

      my_echarts.setOption(option)
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
