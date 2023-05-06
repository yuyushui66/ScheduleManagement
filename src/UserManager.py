import src.User as User
import src.mysqlconn as mysqlconn


class UserManager:

    def __init__(self):
        self.db, self.cursor = mysqlconn.mysqlConnectDefault()
        self.onlineUserIDs = set()
        self.bannedUserIDs = set()

    def userLogin(self, user: User):
        user.status = User.UserStatus.LOGGED_IN
        self.onlineUserIDs.add(user.id)

    def userLogout(self, user: User):
        user.status = User.UserStatus.LOGGED_OUT
        self.onlineUserIDs.remove(user.id)

    def userBan(self, user: User):
        user.status = User.UserStatus.BANNED
        self.bannedUserIDs.add(user.id)

    def userUnban(self, user: User):
        user.status = User.UserStatus.LOGGED_OUT
        self.bannedUserIDs.remove(user.id)

    def getUserInfo(self, userID: int):
        sql="select * from users where id = " + str(userID)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return User.User(data[0], data[1], data[2], data[3], data[4], data[5])

    def getAllUsers(self):
        sql="select * from users"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def getAllBannedUsers(self):
        sql="select * from users where status = 2"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def writeBannedUsers(self):
        for userID in self.bannedUserIDs:
            sql="update users set status = 2 where id = " + str(userID)
            self.cursor.execute(sql)
            self.db.commit()

    def writeUnbannedUsers(self):
        for userID in self.bannedUserIDs:
            sql="update users set status = 1 where id = " + str(userID)
            self.cursor.execute(sql)
            self.db.commit()

