# 工程配置文件
# dialect+driver://username:password@host:port/database?charset=utf8

DIALECT = 'mysql'
DIRVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'py310db'

# 固定写法
# 数据库链接的配置，此项必须，格式为（数据库+驱动://用户名:密码@数据库主机地址:端口/数据库名称）
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DIRVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
# 跟踪对象的修改，目前用不到调高运行效率，所以设置为False
SQLALCHEMY_TRACK_MODIFICATIONS = False