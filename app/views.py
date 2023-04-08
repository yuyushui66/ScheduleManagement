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

        return render(request, 'index.html')

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
    if request.method == 'GET':
        return render(request, 'index.html') # 以GET方式进行响应，就是在浏览器中输入URL，然后回车就会进行这个语句
    else : # 以POST形式进行响应，就是前端网页中的对应位置的数据会被放置在POST中，以map的形式
        return render(request, 'index.html')


def state(request):
    if request.method == 'GET':
        return render(request, 'state.html') # 以GET方式进行响应，就是在浏览器中输入URL，然后回车就会进行这个语句
    else : # 以POST形式进行响应，就是前端网页中的对应位置的数据会被放置在POST中，以map的形式
        return render(request, 'state.html')


