from django.shortcuts import render,HttpResponse
import os, os.path
import json
from app.img_base64_convert import img_base64_convert as conveter
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.http import QueryDict

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
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('GUI_test/')
    else:
        return render(request, 'app/login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('GUI_test/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('login/')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', locals())

def Save_canvas(request):
    if request.method == 'POST':
        #data = json.loads(request.POST.get('line'))
        data = json.loads(request.POST.get('circle'))
        print(data)
    return render(request, 'app/app.html')