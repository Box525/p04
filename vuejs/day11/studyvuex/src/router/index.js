import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Show from '@/components/show/Show'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/datas/:id',
      name: 'datas',
      component: Show
    }
  ]
})
