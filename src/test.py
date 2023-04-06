import pymysql

db = pymysql.connect(host='bj-cynosdbmysql-grp-6afbmg9m.sql.tencentcdb.com', user='root', passwd='Smdb1234', port=24356)
print(type(db))
cursor = db.cursor()
cursor.close()
