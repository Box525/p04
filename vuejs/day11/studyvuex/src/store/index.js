import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 有这样一个问题：用户会设置 无痕浏览模式 相当于设置了 浏览器的不存储

let defaultCity = '大郑州'
try {
  if (localStorage.city) {
    defaultCity = localStorage.city
  }
} catch (error) {
  
}

export default new Vuex.Store({
  state: {
    userName: '村里有个姑娘叫老芳',
    city: defaultCity
  },
  // actions: {
  //   newUserName(ctx,value){
  //     ctx.commit('newUserName',value)
  //   },
  //   emitCity(ctx,value){
  //     ctx.commit('citys','我最喜欢的城市:' + value)
  //   }
  // },
  mutations: {
    newUserName(state,value){
      state.userName = value
      
    },
    citys(state,value){
      state.city = value
      localStorage.city = value
      sessionStorage.city = value
    }
  }
})