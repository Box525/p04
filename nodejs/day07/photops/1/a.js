function sayHi(msg) {
    console.log(msg)
}
function sayHi2(msg) {
    console.log(msg)
}


if (true) {
    let flag = false
    for(let i=0; i<10; i++){
        if (i == 5) {
            // sayHi(i)
            flag = true
            break
        }
    }
    if (flag) {
        sayHi('find')
    }else
        sayHi('end')
}
sayHi('begin..........')





// b.js 函数调用
// callback()



// sum 求和
// return 结果 返回函数调用的位置 同步处理结果 立刻
// callback 用于处理不能确定 结果和时间的时效性，不立刻 耗时
// 效率低 callback 一般情况下 使用在异步处理中

var obj = {}
obj.sum = function (a,b) {
    let sum = a+b
    return sum
}

module.exports = obj