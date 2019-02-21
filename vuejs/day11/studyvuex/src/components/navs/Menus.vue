<template>
  <div>
    <ul>
      <li v-for="(item,index) in menus" 
      :key="index"
      >
        {{ item.mname }}
        <ul>
          <li v-for="(sub_item) in item.submenus" 
          :key="sub_item.smid"
          @click="handleNav(sub_item.smid)"
          >
            {{ sub_item.smname }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
let menus = {
  items: [
    {
      mname: '客户信息',
      mid: '1',
      submenus: [
        {
          smname: '货贷明细',
          smid: '11'
        },
        {
          smname: '费用发放',
          smid: '12'
        }
      ]
    },
    {
      mname: '管理员项',
      mid: '2',
      submenus: [
        {
          smname: '权限分配',
          smid: '21'
        },
        {
          smname: '用户管理',
          smid: '22'
        }
      ]
    }
  ]
}
export default {
  name: 'Menus',
  data() {
    return {
      menus: menus.items
    }
  },
  methods: {
    handleNav(id){
      this.$router.push({name:'datas',params: { id: id }})
    }
  },
}
</script>

<style>

</style>
