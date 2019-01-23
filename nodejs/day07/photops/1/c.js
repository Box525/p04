const a = require('./a')
const b = require('./2/b')

console.log('before')
//return
let sum = a.sum(1,1)
console.log(sum)
console.log('after')

// callback
console.log('before')
let res = b.sum(1,2,function(err,result){
    console.log(result)
})
console.log('res:',res)
console.log('after')