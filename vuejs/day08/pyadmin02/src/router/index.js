import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Product from '@/components/Product'
import ClassInfo from '@/components/ClassInfo'
import ClassPm from '@/components/ClassPm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
		{
		  path: '/home',
		  name: 'home',
		  component: Home,
			children: [
				{
					path: 'product',// /home/product
					name: 'product',
					component: Product
				}
			]
		},
		{
		  path: '/class',
		  name: 'class',
		  component: ClassInfo,
			children: [
				{
					path: ':cid', // /class/:cid
					name: 'cid',
					component: ClassPm
				}
			]
		}
  ],
	mode: 'history' //去掉#
})
