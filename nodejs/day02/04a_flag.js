const fs = require('fs')
// fs.open('./input.txt','a+',(err,fd)=>{
//     if (err) {
//         throw err
//     }
//     fs.readFile('./input.txt', (err, data) => {
//         if (err) {
//             throw err
//         }
//         fs.writeFile(fd, 'hello world2222',{flag:'a'},(err) => {
//             if (err) {
//                 throw err
//             }
//             console.log('写入成功')
//         })
//     })

// })

// fs.readFile('./input.txt', (err, data) => {
//     if (err) {
//         throw err
//     }
//     console.log(data.toString())
//     fs.writeFile('./input.txt', 'hello world', {flag:'a'},(err) => {
//         if (err) {
//             throw err
//         }
//         console.log('写入成功')
//     })
// })

fs.writeFile('./input.txt', 'hello world2222', {
    flag: 'a'
}, (err) => {
    if (err) {
        throw err
    }
    console.log('写入成功')
})

// 1.作业1 能否封装一个 关于文件操作的 自定义模块

// 文件操作的其它API

// 判断是否是 文件或者是目录
fs.stat('./input.txt',(err,stats)=>{
    if (err) {
        throw err
    }

    if (stats.isFile) {
        //是文件
        console.log('是文件')
    }else if (stats.isDirectory) {
        //是目录
        console.log('是目录')
    }   
})

// 创建目录
// fs.mkdir('./myfloder/',err=>{
//     if (err) {
//         throw err
//     }
// })
// fs.rmdir('./myfloder/',err=>{
//     if (err) {
//         throw err
//     }
// })
// 读取一个文件夹
fs.readdir('./homework/',(err,files)=>{
    if (err) {
        throw err
    }
    console.log(files)
})

// 删除文件
fs.unlink('./homework/1122/1.js',err=>{
    if (err) {
        throw err
    }

})

/* 总结
Nodejs 文件系统模块fs 中方法均有 同步和异步版本
异步版本的方法最后一个参数均为回调函数，利用这个回调函数去完成对应文件操作

建议使用异步方法，因为它比同步性能更高，速度更快并且没有阻塞

Nodejs  非阻塞I/O


*/

