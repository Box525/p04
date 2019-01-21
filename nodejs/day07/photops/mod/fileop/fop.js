/* 文件操作 */
const path = require('path')
const fs = require('fs')

/* 判断文件是否存在 */
function check_file(fp) {
    return fs.existsSync(fp)
}
/* 判断目录是否存在 */
function  check_dir(dp) {
    
}

/* cb */
function callBack(exists) {
    
}

/* fp = file path */
function f_open(fp) {
    let f_path= path.join(__dirname, fp)
    // 判断当前文件或者文件目录是否存在
    // check_file(f_path,callBack)
    let res = check_file(f_path)
    if (res) {
        // 文件存在
        
    }else{
        // 文件不存在

    }
}
/* 读取文件 */
function f_read(fp,cb) {

    let f_path = path.join(process.cwd(),fp)
    console.log(f_path)
    // 同步判断
    let res = check_file(f_path)
    if (res) {
        // 异步读取
        fs.readFile(fp, (err, data) => { 
            if(err) throw err;
            // 如何把结果传出去
            // 因为这是异步
            console.log("1111111111111")
            cb(res,data.toString())
            console.log(data.toString())
            console.log("222222222222")
        })
    }else{
        throw `${f_path} 不存在`
    }
}

module.exports = {
    fopen: f_open,
    fread: f_read
}