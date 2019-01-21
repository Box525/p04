/* 用于处理用户验证 */
const fop = require('../fileop/fop')
const path = require('path')
// users.txt /
function oauth_user(user_info,cb) {
    // 读取文件
    // fop.fread('')
    // console.log(__dirname)
    // 获取当前 程序运行的 根目录
    // console.log(process.cwd())
    // 获取当前 程序运行的根目录
    // console.log(path.dirname(require.main.filename))
    // console.log(__filename)
    // console.log(path.dirname(__filename))
    // console.log(require.main.filename)
    fop.fread('sources/users.json',cb)
}


module.exports = {
    oauth : oauth_user
}