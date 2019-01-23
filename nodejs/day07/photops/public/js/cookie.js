// cookie 长度是有效的 4KB
// cookie get 请求的时候会被带上 所以需要设置


function setCookie(cname, cvalue, exdays) {
    let date = new Date()
    date.setTime(date.getTime() + exdays * 24 * 60 * 60 * 1000)

    // 设置cookie 时效
    // let expires = "expires=" + date.toGMTString()

    let expires = "expires=" + date.toUTCString()

    document.cookie = cname + '=' + cvalue + '; ' + expires
}

function getCookie(cname) {
    let ca = document.cookie.split(';')
    for (let i = 0; i < ca.length; i++) {
        let item = ca[i].trim()
        let items = item.split('=')
        if (items[0] == cname) {
            return items[1]
        }
    }
    return ''
}

// document.cookie = ''
// console.log(document.cookie)
// 程序 是无法删除掉一个cookie的key 和 value
// 只能 设置 key 的无效才能让 key 起到 删除作用
function deleteCookie(cname) {
    setCookie(cname, '', 0)
}