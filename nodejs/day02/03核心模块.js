/* 
模块 它是Nodejs中很重要的一个概念
为了能让nodejs 文件可以相互调用，nodejs提供了一个简单模块系统
模块是nodejs应用程序的基本组成部分，文件和模块是一一对应的
也就是说一个js文件就是一个模块
require
*/
// nodejs 自身自带的模块（系统级别、内置）
// fs = file system 文件系统
// 一般来说，对服务器的访问其实就是访问文件

// 如果想对文件进行操作，必须先引入文件模块
const fs = require('fs')

// open(path,flags,mode,callback)
/* 
path: 指定文件路劲(相对、绝对)
flags: 指定打开文件的方式
        r 只读 w 只写 
        r+ 读方式、如果文件不存在则会抛出异常
        w+ 如果文件不存在 则创建文件
        rs 以同步的方式进行读取
        rs+ 以同步的方式进行读取和写入文件
        a 以追加的方式打开一个文件，如果文件不存在就创建
        a+ 同a
callback: 用来处理打开过程中的状态
        err：错误信息
        fd：表示打开后 操作文件的对象
*/
fs.open('./text.txt','r+',(err,fd)=>{
    if (err) {
        // console.log('err:',err)
        throw '这个文件打开失败'
    }
    console.log('打开成功')
})
// 先读
fs.readFile('./text.txt',(err,fd)=>{
    if (err) {
        throw err
    }
    console.log(fd.toString())
})
// 写
let ss = 'hello world!!!!'
let wdata = `这是即将写入的文件信息 ${ ss }`

fs.writeFile('./text.txt',wdata,(err)=>{
    if (err) {
        throw err
    }
})

console.log('finished............')

// 同步
const fs_sync = require('fs')

fs_sync.openSync('./text1.txt','r+')
console.log('同步读开始')
let datas = fs_sync.readFileSync('./text1.txt')

console.log(datas.toString())

console.log('同步读结束')


fs.open('./text1.txt','a',(err,fd)=>{
    if (err) {
        throw err
    }
    console.log('fd:',fd)
})

// 先读后写
fs.readFile('./text1.txt',(err,data)=>{
    if (err) {
        throw err
    }
    console.log('***3333***:',data.toString())
    let new_data = data.toString()
    fs.writeFile('./text1.txt',`${ new_data }`,(err)=>{
        if (err) {
            throw err
        }
    })
})




