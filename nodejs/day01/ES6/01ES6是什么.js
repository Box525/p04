/**
 * ES6
 * ECMAScript6 是JavaScript语言的一代标准
 * 它是在2015年6月正式发布
 * 现在已经到了ES9（ES6~ES9）（ES5、ES6、ES7）
 * 
 * ECMAScript 和 JavaScript是什么关系
 * ECMAScript 是 JavaScript 的语言标准和规范
 * JavaScript 是 ECMAScript 的实现
 */
// 1.变量和字符串
var a_value = 'Hello' //全局变量

if( true ){
    var b_value = 'world'
}
console.log(a_value)
console.log(b_value)
// 为了能解决 JS 的变量被提升问题，也要觉得 全局和局部的概念
// ES6 引入了新的变量声明方式 1. let 2.const

// let 局部变量 
// 对于编程语言来说，{ } 表示作用域

if(true){
    var c_value = 123
    let d_value = 456
    console.log(d_value)
}

// console.log(d_value)
// console.log(e_value)
let e_value = '20190111'
console.log(e_value)

// 笔试题
function func() {
    var aaa = 18
    var bbb = 20
    if(true){
        let aaa = 100
        var bbb = 200
    }
    console.log(aaa) //18
    console.log(bbb) //20 200
}
func()

// 场景一 见index.html


let a = 1
// let a = 2
console.log(a)
var b = 2
var b = 2
console.log(b)
// let 声明的变量不能被重复定义/声明


// const 声明的是常量 一旦声明，值将不会变
const PI = 3.1415926

// PI = 3.14
// const 也是有作用域之说 和 let 一样有作用域 一样也不能重复声明

if (true) {
    const abc = 'abc'
}
// console.log(abc)


// 2.string 字符串
// ES5 string
let a_string = 'hello world'
// indexOf 返回第一次出现指定字符串的位置下标 如果没有则返回-1
let index = a_string.indexOf('world')
console.log(index)
index = a_string.indexOf('world',7)
console.log(index) 

// 作业 查找指定字符串中出现最多的字母，并统计出现的次数
// 比如  aabcaancdddac

//
let rets = a_string.split(' ')
console.log(a_string)
console.log(rets)

// ES6 中对String方法进行扩展
// hello world
// startsWith() 返回布尔值，表示参数字符串是否在源字符串的在指定位置的开始位置，默认是从头部开始
console.log(a_string.startsWith("hello"))
console.log(a_string.startsWith("world"))
console.log(a_string.startsWith("world", 6))
// endsWitn()
// includes()
console.log(a_string.includes('or'))

// repeat(n) 指定字符串重复n次
let b_string = 'aaabbbbcccc'
console.log(b_string.repeat(3))

// 模板字符串
let firstName = 'Tom'
let lastName = 'Ads'

let totleName = `hello ${firstName} ${lastName}`
let tt = `sum: ${1>2?true:false} ${firstName + lastName}`

console.log(totleName)
console.log(tt)

let lines_string = `
    1
    2
    3
    4
    5
    6
    7
    8
`
console.log(lines_string)

// 3 数组
// 扩展运算符
// 作用是 将一个数组转为一个参数序列
console.log(...[1,2,3,4])

// 实现讲一个数组添加到另外一个数组中
function my_push(array, items) {
    array.push(...items)
}

let b_array = [1,2,3,4]
my_push(b_array,[4,5,6,7])
console.log(b_array)

function add(a,b,c,d) {
    return a+b+c+d
}

let args = [1,2,3,4]
console.log(add(...args))

let c_array = [1,2,3,4,5,6,7]
c_array.forEach(function (value,index) {
    console.log(index,value)
})

// for (const key in object) {
//     if (object.hasOwnProperty(key)) {
//         const element = object[key];
        
//     }
// }

for( let item in c_array){
    console.log(item,c_array[item])
}

let obj = new Object()
obj.name = 'Tom'
obj.age = 18

for( const key in obj){
    console.log(key)
    if (obj.hasOwnProperty('sex')) {
        console.log(true)
    }else{
        console.log(false)
    }
}

// ES6 对数组扩展了3个方法
// keys() 键名遍历
// values() 键值遍历
// entries() 键值对遍历
for(let index of ['a','b'].keys()){
    console.log(index)
}

for (let index of ['a', 'b'].values()) {
    console.log(index)
}

for (let [index,value] of ['a', 'b'].entries()) {
    console.log(index,value)
}


// 函数
// ES6 改进函数的表达
// ES5的函数表达
function func_name(pars) {
    //函数体
}

// ES6的箭头函数
var a_func = (()=>{
    return 'hehe'
})()

// (()=>())()

console.log(a_func)

c_array.forEach(function (value, index) {
    console.log(index, value)
})

c_array.forEach((value,index)=>{
    console.log(this)
    console.log(index,value)
})