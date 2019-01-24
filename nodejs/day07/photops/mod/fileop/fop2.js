/* 封装文件操作模块 */
const fs = require('fs')
const path = require('path')

// 拼接全路径
function full_path(fp) {
    return path.join(process.cwd(),fp)
}

// 是否是文件
function is_file(fp,cb) {
    // 2.异步判断文件是否存在
    fs.exists(fp,function (exists) {
        // exists true 表示是文件
        cb(exists)
    })
}

function f_read(fp,cb) {
    fp = full_path(fp)
    // 1.判断是否是文件
    is_file(fp,function (res) {
        if(res){
            // 3.读取文件
            fs.readFile(fp,function (err,data){
                if(err) throw err
                // console.log(data.toString())
                cb(null,data.toString())
            })
        }else{
            console.log('文件不存在')
            cb(res,null)
        }
    })
}

// f_read('sources/users.json',function (err,data) {
//     if(err) throw err
//     console.log(data)
// })

// 写文件
function f_write(fp,info,cb) {
    fp = full_path(fp)
    console.log(fp)
    is_file(fp,function (res) {
        if (res) {
            fs.readFile(fp,function (err,data) {
                if (err) {
                    throw err
                }
                let obj = data.toString()
                console.log(obj)
                // '' null
                if (obj != '' || obj != null) {
                    obj = JSON.parse(obj)
                    if(obj.hasOwnProperty('users')){
                        obj['users'].push(info)
                    }else{
                        obj['users'] = []
                        obj['users'].push(info)
                    }

                    obj = JSON.stringify(obj)
                    fs.writeFile(fp,obj,(err)=>{
                        if (err) {
                            throw err
                        }
                        cb(null,'写入成功')
                    })

                }else{
                    console.log('没有内容')
                    cb(null, '没有内容')
                }

            })
        }else{
            cb(res,'文件不存在')
        }
    })
}

/* 修改用户信息 
1.用户查找
2.用户信息修改
3.保存
*/
function f_edit(fp,info,cb) {
    
}



/* let info = {
    uname: 'Jack',
    uage: 18
}
f_write('./users.json',info,function (err,res) {
    if (err) {
        throw err
    }
    console.log(res)
}) */

// 读取用户s目录
// dp = dir path
// eg: sources/users/
function r_dir(dp,cb) {
    dp = full_path(dp)
    // 判断目录是否存在
    fs.readdir(dp,(err,files)=>{
        if(err){
            cb(false,null)
        }
        cb(null,files)
    })
}

/* 创建用户目录 */
// dp 用户目录：/sources/users/Tom
// 图片目录: /sources/users/Tom/创建目录的规则(采用的是时间)
function f_mkdir(dp,cb) {
    dp = full_path(dp)
    // 判断
    is_file(dp,(res)=>{
        if (!res) {
            fs.mkdir(dp, (err) => {
                if (err) {
                    cb(true, {
                        msg: '创建失败',
                        code: '6001'
                    })
                }
                cb(false,{
                    msg:'文件创建成功',
                    code:''
                })
            })
        }else{
            cb(false,{
                msg:'文件已存在',
                code:''
            })
        }
    })
    
}

// 开放接口
module.exports = {
    fread: f_read,
    fwrite: f_write,
    rfiles: r_dir,
    fmkdir: f_mkdir
}