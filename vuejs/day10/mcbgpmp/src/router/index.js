import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import MCLogin from '@/components/login/MCLogin'
import MCHome from '@/components/Home/MCHome'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'home',
      component: MCHome
    },
    {
      path: '/login',
      name: 'login',
      component: MCLogin
    }
  ],
  mode: 'history'
})
