// 本页的函数
// 声明一个函数
function sum(a,b) {
    return a+b
}

var ret = sum(1,1)
console.log(ret)

// 调用文件外的js文件
// require() 引入/导入一个模块 js文件
var sayHi2 = require('./index.js') //require('./index')
sayHi2('hell node js!!!')

var says = require('./index01')
// says.sBB('11111111111')
// says.sH('33333333333333')
says.sayBye('12334')
says.sayHello('abcd')