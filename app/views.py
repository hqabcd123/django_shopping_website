from django.shortcuts import render,HttpResponse
import os, os.path
import json
from app.img_base64_convert import img_base64_convert as conveter

def home(request):
    #return render(request, 'index.html')
    return render(request, 'app/app.html')

def GUI_test(request):
    current_path = os.path.dirname(__file__)
    DIR = '..\Media'
    DIR = os.path.join(current_path, DIR)
    print (DIR)
    img_dir = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]
    print (img_dir)
    Json_img_dir = json.dumps(img_dir)
    print (Json_img_dir)
    #print ([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    return render(request, 'app/GUI_test.html', locals())

def login(request):
    ##
    return render(request, 'app/login.html', locals())