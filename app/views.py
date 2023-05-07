'''
Date: 2023-04-03 14:23:14
LastEditors: MrZ2001 735108298@qq.com
LastEditTime: 2023-04-03 14:47:53
FilePath: \ScheduleManagement\app\views.py
Description: 
'''
import json
import random
from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import zipfile
import sys

import src.Communication
from app import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

import src.Communication as cm
import src.mysqlconn as mysqlconn
from src.UserManager import UserManager
from src.User import User
import hashlib

import re

u = User(0)
um = UserManager()

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValidEmail(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


@csrf_exempt
# request是一个对象，在其中封装了浏览器发送来的所有请求相关数据
def login(request):
    print(request.method)

    if request.method == 'GET':
        return render(request, 'login.html')
        # return HttpResponse("欢迎使用")
    else:
        email = request.POST.get("username")
        pwd = request.POST.get("password")
        is_keep = request.POST.get("Field")

        # 此处应该判断密码及用户在数据库中是否有匹配的项，若有则执行下面语句index.html，若无login.html
        # if username in mysql and pwd in mysql:

        sql = "select password from users where email = " + "'" + email + "'" + ";"
        User.cursor.execute(sql)
        correct_pwd = User.cursor.fetchall()
        correct_pwd = correct_pwd[0][0]


        pwd = hashlib.sha224(pwd.encode('utf-8')).hexdigest()

        if pwd == correct_pwd:
            return redirect('/index/')
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})



@csrf_exempt
def signup(request):
    print(request.method)

    if request.method == 'GET':
        return render(request, 'signup.html')
        # return HttpResponse("欢迎使用")
    else:
        name = request.POST.get("firstname") + ' ' + request.POST.get("lastname")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        re_pwd = request.POST.get("confirm_password")
        isaccpt = request.POST.get("Field")
        print(name, email, pwd, re_pwd, isaccpt)
        # 正则判断输入是否合法，合法则插入数据库

        # test if email is valid.

        res = isValidEmail(email)
        if not res:
            return render(request, "signup.html", {"error_msg": "邮箱格式不正确"})
        elif pwd != re_pwd:
            return render(request, "signup.html", {"error_msg": "两次密码不一致"})
        else:
            if u.isDuplicatedEmail(email):
                return render(request, "signup.html", {"error_msg": "该邮箱已被注册"})
            else:
                u.register(name, email, pwd)
                return render(request, "login.html", {"success_msg": "注册成功，请登录"})

        # return render(request, 'signup.html')


def index(request):
    data = []
    c = cm.Communication()
    sql = "select * from tasks;"
    res = c.readFromDB(sql, False)
    NewestId = 0
    for i in res:
        new_result = [
            i[1],
            "_fc" + str(i[0]),
        ]
        if i[6] is None:
            new_result.append('null')
        else:
            new_result.append(i[6].strftime("%a %b %d %Y %H:%M:%S GMT+0800 (中国标准时间)"))
        if i[7] is None:
            new_result.append('null')
        else:
            new_result.append(i[7].strftime("%a %b %d %Y %H:%M:%S GMT+0800 (中国标准时间)"))
        if i[-1] == 'true':
            new_result.append('true')
        else:
            new_result.append('false')
        data.append(new_result)
        if i[0] > NewestId: NewestId = i[0]

    NewestId = NewestId + 1
    file = open('static/js/full-calendar/id.txt', 'w', encoding='utf-8')
    file.write(str(NewestId))
    file.close()

    # print(data)
    data = json.dumps(data)  # data必须是一个list
    if request.method == 'GET':
        return render(request, 'index.html', locals())  # 以GET方式进行响应，就是在浏览器中输入URL，然后回车就会进行这个语句
    else:  # 以POST形式进行响应，就是前端网页中的对应位置的数据会被放置在POST中，以map的形式
        return render(request, 'index.html', locals())


def state(request):
    if request.method == 'GET':
        return render(request, 'state.html')  # 以GET方式进行响应，就是在浏览器中输入URL，然后回车就会进行这个语句
    else:  # 以POST形式进行响应，就是前端网页中的对应位置的数据会被放置在POST中，以map的形式
        return render(request, 'state.html')


def reports(request):
    if request.method == 'GET':
        return render(request, 'reports.html')
    else:
        return render(request, 'reports.html')
