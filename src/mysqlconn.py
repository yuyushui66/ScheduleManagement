import pymysql


def mysqlConnect(_host: str, _user: str, _passwd: str, _port: int = 3306):
    db = pymysql.connect(host=_host, user=_user, passwd=_passwd, port=_port)
    print("Connected.")
    cursor = db.cursor()
    return db, cursor


# 打开数据库连接
try:
    db = pymysql.connect(host='localhost', user='root', passwd='zcx.11123', port=3306)
    print('连接成功！')
except:
    print('Connection Failed!')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone() # single
# data = cursor.fetchall() # all

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

'''
连接成功！
Database version : 8.0.25 
'''
