import pymysql
import src.mysqlconn as mysqlconn


class Communication:
    def __init__(self):
        self.db, self.cursor = mysqlconn.mysqlConnectDefault()

    def writeToDB(self, sql, printFlag=True):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            ret = self.cursor.fetchall()
            if printFlag:
                print(ret)
            return True
        except pymysql.err.Error as e:
            print(e.args[0])
            print(e)
            self.db.rollback()
            return False

    def readFromDB(self, sql, printFlag=True):
        try:
            self.cursor.execute(sql)
            ret = self.cursor.fetchall()
            if printFlag:
                print(ret)
            return ret
        except pymysql.err.Error as e:
            print(e.args[0])
            print(e)
            self.db.rollback()
            return ''
