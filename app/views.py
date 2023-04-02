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
    else :
        return render(request, 'login.html')
