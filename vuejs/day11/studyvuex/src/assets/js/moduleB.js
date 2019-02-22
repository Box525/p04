
// export var name = '王校长'

// var name = '王校长'
// var name2 = '王校长的OMG'

// export default {
//   name,
//   name2
// }

function People(dict) {
    this.age = dict.age
    this.name = dict.name
}

export default new People({
    name: '小明',
    age: 18
})