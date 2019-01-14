function sayHi(msg) {
    console.log(msg)
}

function sayBye(msg) {
    console.log(msg)
}

function callBackFn(fn,msg) {
    fn(msg)
}

callBackFn(sayHi,'hello')

// 回调的典型方式： 是将函数名最为参数进行传递 在需要的时候进行调用
