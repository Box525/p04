function callback(fn) {
    let msg = ''
    fn(msg)
}

var obj = {}
obj.sum = function (a,b,callback) {
    // let sum = a + b
    // callback(null,sum)
    setTimeout(function () {
        let sum = a + b  
        // callback(null,sum)
        return sum
    },2000)
}

module.exports = obj

