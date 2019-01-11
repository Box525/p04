function sum(a,b) {
    return a+b
}

function sayBye(msg) {
    console.log(msg,sum(1,1))
}

function sayHello(msg) {
    console.log(msg)
}
/*
module.exports = {
    sBB : sayBye,
    sH : sayHello
}*/

module.exports = {
    sayBye,
    sayHello
}