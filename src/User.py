import datetime
from itertools import count

import pymysql

from mysqlconn import mysqlConnect, mysqlConnectDefault
from enum import Enum
import hashlib


class UserStatus(Enum):
    LOGGED_IN = 0
    LOGGED_OUT = 1
    BANNED = 2


class User:
    UserIDCounter = count(0)

    def __init__(self, _id: int, _name: str = "User", _email: str = "", _avatar: str = "",
                 _password: str = hashlib.sha224("000000"),
                 _status=UserStatus.LOGGED_OUT):
        self.id = _id
        self.name = _name
        self.email = _email
        self.avatar = _avatar
        self.password = _password
        self.status = _status

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

    # setter
    def setName(self, _name: str):
        self.name = _name

    def setEmail(self, email: str):
        self.email = email

    def setAvatar(self, avatar: str):
        self.avatar = avatar

    def setPassword(self, password: str):
        self.password = password

    # other functions
    db, cursor = mysqlConnectDefault()

    def login(self, _password):
        sql = "select password from users where id = " + str(id)
        User.cursor.execute(sql)
        pwd = User.cursor.fetchall()
        _password = hashlib.sha224(_password)
        if pwd == _password:
            self.status = UserStatus.LOGGED_IN
            return True
        else:
            return False

    def logout(self):
        self.status = UserStatus.LOGGED_OUT

    @staticmethod
    def isDuplicatedEmail(_email):
        sql = "select email from users where email = " + _email
        User.cursor.execute(sql)
        email = User.cursor.fetchall()
        if email == _email:
            return True
        else:
            return False

    @staticmethod
    def register(_name, _email, _password):
        """
        desc: This function is used to register a new user.
        :(1) check if the email is duplicated
        :(2) if not, insert the new user into the database
        :(3) return the id of the new user
        :(4) if the email is duplicated, return -1
        :(5) if there is an error, return -2
        :param _name:
        :param _email: should be unique
        :param _password: get original password and hash it by sha224
        :return: int
        """
        if User.isDuplicatedEmail(_email):
            return -1
        _password = hashlib.sha224(_password)
        try:
            _id = next(User.UserIDCounter)
            sql = "insert into users values(" + str(_id) + ", " + _name + ", " + _email + ", " + str(
                _password) + ", " + ")"
            User.cursor.execute(sql)
            User.db.commit()
            return id

        except pymysql.Error as e:
            print(e)
            User.db.rollback()
            return -2

    def delete(self):
        sql = "delete from users where id = " + str(self.id)
        User.cursor.execute(sql)
        User.db.commit()

    def update(self, _name, _email, _password, _birthDate):
        _password = hashlib.sha224(_password)
        sql = "update users set name = " + _name + ", email = " + _email + ", password = " + str(
            _password) + " where id = " + str(self.id)
        User.cursor.execute(sql)
        User.db.commit()

    def isBanned(self):
        return self.status == UserStatus.BANNED

    def isLogged(self):
        return self.status == UserStatus.LOGGED_IN

    def __str__(self):
        return "User: " + self.name + " " + str(self.id)

    def __repr__(self):
        return self.__str__()
