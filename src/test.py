import pymysql

db = pymysql.connect(host='bj-cynosdbmysql-grp-6afbmg9m.sql.tencentcdb.com', user='root', passwd='Smdb1234', port=24356, database='SMDB')
cursor = db.cursor()

# sql = "insert into user values(1, 'test', 'test', 'test', 1)"
# cursor.execute(sql)
# db.commit()
# ret = cursor.fetchall()
# print(ret)


sql = "insert into users values(1, 'test', 'test', 'test', 1)"
try:
    cursor.execute(sql)
    db.commit()
    ret = cursor.fetchall()
    print(ret)
except pymysql.err.Error as e:
    print(e.args[0])
    print(e)
    db.rollback()



db.close()