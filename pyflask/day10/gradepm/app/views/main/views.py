from . import main
from flask import render_template,url_for,redirect,request,session

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
import time

from app.models.admin.admin import Admin
from app.models.gleader.gleader import GLeader

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/favicon.ico')
def facicon():
    return ''

@main.route('/index')
def index2():
    return render_template('main/index1.html')

def set_serializer(msg):
    salt = 'salt'
    ser = Serializer(salt, expires_in=600)
    return ser.dumps(msg).decode()


def get_serializer(msg):
    salt = 'salt'
    ser = Serializer(salt, expires_in=600)
    try:
        res = ser.loads(msg)
        return res
    except BadSignature as e:
        print(e)
        return render_template('error/404.html')
    except SignatureExpired as e:
        print(e)
        return render_template('error/404.html')





@main.route('/addgrade',endpoint="add_grade")
def addGrade():
    cookie = request.cookies
    print(cookie.get('token'))
    res = get_serializer(cookie.get('token'))
    print(res)
    if type(res) is str:
        return res
    else:
        admin = Admin.query.filter(Admin.aname == res['uname']).first()
        if admin:
            gleaders = GLeader.query.with_entities(GLeader.id,
                                                   GLeader.lname).all()

            return render_template('main/index1.html', addGrade=True,gleaders=gleaders)
        else:
            return 'not fount'

    return render_template('main/index1.html',addGrade=True)


@main.route('/savegrade',endpoint='save_grade')
def saveGrade():
    # cookie 根据浏览器不同存储大小也不一样，最大4KB
    # session 作用和cookie 类似 它们都是为了存储用户的相关信息
    # 不同的是：cookie 是存储在本地浏览器 而session 存储在服务器
    # session 把用户数据存储在服务器上了，不容易被窃取 相对安全
    # 但是也有弊端：会占用服务资源，但是这个弊端对于现代服务器来说可以被忽略

    # 在flask中使用 session
    # from flask inport session
    # import os
    # import datetime import timedelta
    # 设置 session
    session['uname'] = 'admin'
    session.permanent = True
    print(session)

    # session 时效
    # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
    # permanent:过期时间，默认是False 如果是True 则31天之后过期
    #session.permanent = True #False

    # 1.添加 班级数据表

    # 2.将获取到所有的数据 传递给 主页

    return 'set_session'#render_template('main/index1.html')

@main.route('/session')
def getSession():
    if 'uname' in session:
        print('***********************')
        print(session.get('uname'))
    else:
        print('()()()()()()')
        print(session)

    return 'session 存储的用户是:%s' % session.get('uname')


########正则表达式############
'''
正则表达式：是一个特殊的字符序列，也称规则表达式
Regular Expression
在编程中，经常以简写的方式出现：regex \ re
作用：是用来检查一个字符串是否与某种模式(规则)匹配
正则是使用C编写的匹配引擎执行
场景
1.给定的字符串是否符合正则表达式的过滤逻辑（匹配）（手机号、邮箱、密码等）
2.可以通过正则表达式，从字符串中获取想要的特定部分
search 和 match
'''
#使用正则 需要引入模块re 该模块属于Python自带模块
import re

def stringRe():
    #正则表达式涉及到的字符，分2种
    # 1.普通字符 2.元字符 （具有特殊功能的字符）
    # 1. 普通字符
    find_all = re.findall('abc','abcdabceababcabcd')
    print(find_all)

def stringReMeta():
    #正则表达式中的元字符
    #11个 ： . ^ $ * + ? {} [] \ | ()
    # 1. '.' 表示 通配符，可以代指所有字符，除了换行符'\n',一个点对应一个字符
    # reg = re.findall('h...o','hello world! he\nlpo')
    # print(reg)
    # 2. ^ 表示从整个字符串开始的位置匹配
    # reg = re.findall('^ah...o','ahello world')
    # print(reg)
    # 3. $ 和 ^ 相反 是从字符串的结尾开始匹配
    # reg = re.findall('h...o$','hello world')
    # print(reg)
    # reg = re.findall('^h...o$','hello')
    # print(reg)
    # 4. * 重复匹配（表达式中的*表示重复 * 号前边的字符，个数冲0到无穷大）
    # 普通写法
    # reg = re.findall('h.........d','hello world')
    # 重复写法
    # reg = re.findall('h.*d', 'hello world hhhd')
    # print(reg)
    # reg = re.findall('w.*','hello world,word!')
    # print(reg)
    # reg = re.findall('wa*', 'hello world,waaaaaaaard!')
    # print(reg)
    # reg = re.findall('f*','golf')
    # print(reg)
    # 5. + 和 * 功能类似，个数是1到无穷大
    # reg = re.findall('f+', 'ffgolf')
    # print(reg)
    # reg = re.findall('a+b','abcabcdaabcacdb')
    # print(reg)
    # reg = re.findall('.+b', 'abcabcdaabcacdba')
    # print(reg)
    # 6. ? 表示匹配 ？ 号前面的字符，个数为闭区间[0,1] 也就是要么0个要么1个
    # reg = re.findall('a?b?','abcabcdaabcacdb')
    # print(reg)
    # 7. {} 表示匹配 {} 前面的字符，指定个数为 {N} 里面的数值N
    # reg = re.findall('a{2}b','abaabaaab') #aab
    # print(reg)
    # 普通字符 如果{}中没有任何数字则 表示 {} 它只是2个普普通通的字符一个是'{' 一个是 '}'
    # reg = re.findall('a{}b','aaaa{}b')
    # print(reg)
    # reg = re.findall('a{1,3}b', 'abaabaaab')  #ab aab aaab
    # print(reg)
    # 8. [] 表示一个字符集，字符的集合，常常用来指定一个字符类别
    #字符可以单独列出来，也可以通过 '-'号分隔的2个给定字符来表示
    #字符区间，匹配区间中的任意一个字符
    # []里面的内容，表示或者的关系，也就是说只要出现任意中括号的内容就匹配
    # reg = re.findall('[a,b,c]d','adbdcdabcd')
    # print(reg)
    # reg = re.findall('[a-c]d', 'adbdcdabcd')
    # print(reg)
    #判断 全部是由小写字母组成的字符串
    # reg = re.findall('[a-z]','456abcAdefgz123')
    # print(reg)
    # reg = re.findall('[0-9,a-z]', '456abcAdefgz123')
    # print(reg)
    # reg = re.findall('[0-9a-zA-Z]', '456abcAdefgz123')
    # print(reg)
    # #[^]中的^ 表示 非的意思 也是除了的意思
    # reg = re.findall('[^0-9a-zA-Z]', '4@56abcAdefgz123')
    # print(reg)
    # reg = re.findall('[^0-9,a-z,A-Z]', '456abcAdefgz123')
    # print(reg)
    # 9.  \ 反斜杠
    # 反斜杠后面跟元字符，表示去除其特殊功能反斜杠
    # 反斜杠后面是普通字符，表示增加了特殊功能
    '''
    \d 表示匹配任何十进制数，相当于[0-9]
    \D 表示匹配任何非十进制数，相当于[^0-9]
    \s 表示匹配任何空白字符，相当于[\t\n\r\f\v]
    \S 和\s相反
    \w 表示匹配任何字母数字字符，相当于 [a-zA-Z0-9]
    \W 和\w相反
    \b 表示匹配一个单词的边界，也就是匹配字符和空格间的位置
    '''
    # reg = re.findall(r'd\b','hello world this is a bada')
    # print(reg)
    #10. () 表示分组，将括号中的内容，当做整体来匹配
    # reg = re.findall('(6666)','a66666a6666$abbc666cddd66')
    # print(reg)
    # reg = re.findall('(6666)+', 'a66666a6666$abbc666cddd66')
    # print(reg)
    # reg = re.search('(6666)', 'a66666a6666$abbc666cddd66').group()
    # print(reg)
    # reg = re.search('(6666)+', 'a66666a6666$abbc666cddd66').group()
    # print(reg)
    # ig.wang001/ig.hello002/ig.hoho003
    # src = 'igwang001/ighello002/ighoho003/'
    # pattern = '(?P<name>\w{6})(?P<id>\d{3})/'
    # reg = re.findall(pattern,src)
    # print(reg)
    # reg = re.search(pattern,src).group()
    # print(reg)
    # reg = re.search(pattern, src)
    # print(reg.group('id'),reg.group('name'))
    # 11. | 管道符 表示逻辑上的 或者
    # reg = re.findall('(he)|wo',('hello world ahewod'))
    # print(reg)
    # reg = re.findall('(he)|(2)', ('he2222'))
    # print(reg)

    #######验证QQ号、手机号、邮箱、身份证、用户名、密码###########
    '''
    QQ:
    特征：1.最少5位，最长11位 2.5位是从10001开始 3.qq:或者QQ:开头

    '''
    # '[1-9]\d{4,10}'

    '''
    邮箱：xxxx@xxx.com/cn/net
    1. @ 前面的字符可以是数字、字母、下划线、中划线或者 .
    2. @ 后面的可以是xx.com xxxx.cn xxxx.com.cn
    '''
    # '\w{0,19}@\w{1,13}\.[com,cn,net]{1,3}'
    #pattern = r'(\w{0,19}@\w{1,13}\.[com,cn,net]{1,3}(.cn)?)'
    # pattern = r'([_a-z.-A-Z0-9]{0,19}@\w{1,13}\.[com,cn,net]{1,3}(.cn?))'
    # reg = re.findall(pattern,'_www_w-1-2-3@qq.com.cn')
    # print(reg)

    '''
    手机号
    1.11位
    2.第一位1 第二位[3-9] 第三位[0-9]
    '''
    #'^1[3-9]\d{9}'

    '''
    身份证:
    1 11111 1 1 11 11 11 111 X
    1 11111 1 9 98 01 31 
    1:地区 1-8 [1-8]
    2-6: [0-9]{5}
    第七位：[12]
    8,9,10 : [0-9]{3} #年的后3位
    11,12: (0[1-9]|1[0-2])
    13,14: (0[1-9]|1[0-9]|2[0-9]|3[0-1])
    15,16,17 [0-9]{3} \d{3}
    18 [0-9]|X|x
    '''
    # ^[1-8]\d{5}[1-2]\d{3}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])\d{3}\d|X|x


    '''
    用户名：
    必须以字母开头，长度不超过10 超过6
    '''
    # ^[a-zA-Z]\w{5,9}

    '''
    密码：
    任意字符 6~18
    '''
    # .{6,18}
    # ^[A-Z].{5,17}

@main.route('/re')
def regex():
    #字符串匹配
    # stringRe()
    #元字符（11个）
    stringReMeta()
    return '正则表达式'

from app.models.role.rlimit import RLimit
from app.models.role.role import Role
# 用户管理 权限设置
@main.route('/roleinfo', endpoint='role_info')
def roleInfo():
    roles = Role.query.with_entities(Role.id,Role.rname).all()
    return render_template('main/index1.html',roleInfo=True,roles=roles)


@main.route('/addlimit', endpoint='add_role', methods=['POST'])
def addLimit():
    # role = Role(rname='超级管理员')
    # role.save()

    # limit1 = RLimit(rlname='添加用户')
    # limit2 = RLimit(rlname='添加班级')
    # limit3 = RLimit(rlname='删除用户')
    # limit4 = RLimit(rlname='删除班级')

    # limit1.save()
    # limit2.save()
    # limit3.save()
    # limit4.save()

    # role = Role.query.filter(Role.rname == '超级管理员').first()
    # ls = RLimit.query.all()
    # for item in ls:
    #     role.limits.append(item)
    # role.save()

    # role = Role.query.filter(Role.rname == '超级管理员').first()
    # print(role.limits)

    # role = Role(rname='班主任')
    # l1 = RLimit.query.filter(RLimit.id == 2).first()
    # l2 = RLimit.query.filter(RLimit.id == 4).first()
    # role.limits.append(l1)
    # role.limits.append(l2)
    # role.save()


    return '创建limits 成功'
