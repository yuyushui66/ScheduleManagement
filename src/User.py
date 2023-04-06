import datetime
from itertools import count
from mysqlconn import mysqlConnect, mysqlConnectDefault
from enum import Enum


class UserStatus(Enum):
    LOGGED_IN = 0
    LOGGED_OUT = 1
    BANNED = 2


class User:
    UserIDCounter = count(0)

    def __init__(self):
        self.id = next(User.UserIDCounter)
        self.name = "User"
        self.email = ""
        self.avatar = ""
        self.password = "000000"
        self.birthDate = datetime.datetime.now()
        self.status = UserStatus.LOGGED_OUT

    # getter
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getAvatar(self):
        return self.avatar

    def getPassword(self):
        return self.password

    def getBirthDate(self):
        return self.birthDate

    # setter
    def setName(self, name: str):
        self.name = name

    def setEmail(self, email: str):
        self.email = email

    def setAvatar(self, avatar: str):
        self.avatar = avatar

    def setPassword(self, password: str):
        self.password = password

    def setBirthDate(self, birthDate: datetime):
        self.birthDate = birthDate

    # other functions
    db, cursor = mysqlConnectDefault()

    def login(self, _password):
        sql = "select password from users where id = " + str(id)
        User.cursor.execute(sql)
        pwd = User.cursor.fetchall()
        if (pwd == _password):
            self.status = UserStatus.LOGGED_IN
            return True
        else:
            return False

    def logout(self):
        self.status = UserStatus.LOGGED_OUT

    def register(self, _name, _email, _password, _birthDate):
        sql = "insert into users values(" + str(
            self.id) + ", " + _name + ", " + _email + ", " + _password + ", " + _birthDate + ")"
        User.cursor.execute(sql)
        User.db.commit()
        name = _name
        email = _email
        password = _password
        birthDate = _birthDate

    def delete(self):
        sql = "delete from users where id = " + str(self.id)
        User.cursor.execute(sql)
        User.db.commit()

    def update(self, _name, _email, _password, _birthDate):
        sql = "update users set name = " + _name + ", email = " + _email + ", password = " + _password + ", birthDate = " + _birthDate + " where id = " + str(
            self.id)
        User.cursor.execute(sql)
        User.db.commit()

    def ban(self):
        self.status = UserStatus.BANNED

    def unban(self):
        self.status = UserStatus.LOGGED_OUT

    def isBanned(self):
        return self.status == UserStatus.BANNED

    def isLogged(self):
        return self.status == UserStatus.LOGGED_IN

    def __str__(self):
        return "User: " + self.name + " " + str(self.id)

    def __repr__(self):
        return self.__str__()
