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
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
        # return HttpResponse("欢迎使用")
    else:
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


