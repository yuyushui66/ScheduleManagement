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
from app import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

@csrf_exempt
# request是一个对象，在其中封装了浏览器发送来的所有请求相关数据
def login(request):
    print(request.method)

    if request.method == 'GET':
        return render(request, 'login.html')
        # return HttpResponse("欢迎使用")
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        is_keep = request.POST.get("Field")
        print(username, pwd, is_keep)
        
        # 此处应该判断密码及用户在数据库中是否有匹配的项，若有则执行下面语句index.html，若无login.html
        # if username in mysql and pwd in mysql:
        if username == 123 and pwd == 123:
            return render(request, 'index.html')
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})

@csrf_exempt
def signup(request):
    print(request.method)

    if request.method == 'GET':
        return render(request, 'signup.html')
        # return HttpResponse("欢迎使用")
    else:
        name = request.POST.get("firstname")+request.POST.get("lastname")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        re_pwd = request.POST.get("confirm_password")
        isaccpt = request.POST.get("Field")
        print(name, email, pwd, re_pwd, isaccpt)
        # 正则判断输入是否合法，合法则插入数据库

        return render(request, 'signup.html')
    
def index(request):
    data = [['栗佳伟', '666', 'Mon May 13 2023 00:00:00 GMT+0800 (中国标准时间)', 'Mon May 13 2023 00:00:00 GMT+0800 (中国标准时间)', 'true'],
            ['余德水', '667', 'Mon May 14 2023 00:00:00 GMT+0800 (中国标准时间)', 'Mon May 14 2023 00:00:00 GMT+0800 (中国标准时间)', 'true'],
            ['郑丞秀', '668', 'Mon May 15 2023 00:00:00 GMT+0800 (中国标准时间)', 'null', 'true'],
            ['闫志杰', 'hh', 'Mon May 4 2023 16:00:00 GMT+0800 (中国标准时间)', 'Mon May 6 2023 18:00:00 GMT+0800 (中国标准时间)', 'true'],]
    data = json.dumps(data)  # data必须是一个list
    if request.method == 'GET':
        return render(request, 'index.html',locals()) # 以GET方式进行响应，就是在浏览器中输入URL，然后回车就会进行这个语句
    else : # 以POST形式进行响应，就是前端网页中的对应位置的数据会被放置在POST中，以map的形式
        return render(request, 'index.html',locals())


def state(request):
    if request.method == 'GET':
        return render(request, 'state.html') # 以GET方式进行响应，就是在浏览器中输入URL，然后回车就会进行这个语句
    else : # 以POST形式进行响应，就是前端网页中的对应位置的数据会被放置在POST中，以map的形式
        return render(request, 'state.html')

def reports(request):
    if request.method == 'GET':
        return render(request, 'reports.html')
    else :
        return render(request, 'reports.html')


