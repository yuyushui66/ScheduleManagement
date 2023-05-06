import pymysql
import mysqlconn

class Communication:
    def __init__(self):
        self.db, self.cursor = mysqlconn.mysqlConnectDefault()

    def writeToDB(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            ret = self.cursor.fetchall()
            print(ret)
        except pymysql.err.Error as e:
            print(e.args[0])
            print(e)
            self.db.rollback()

    def readFromDB(self, sql):
        try:
            self.cursor.execute(sql)
            ret = self.cursor.fetchall()
            print(ret)
        except pymysql.err.Error as e:
            print(e.args[0])
            print(e)
            self.db.rollback()