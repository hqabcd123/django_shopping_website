from curses.textpad import rectangle
import random
import string
from time import timezone
from urllib import response
from venv import create
from django.shortcuts import render,HttpResponse
from django.http.response import JsonResponse
import os, os.path
import json
from .models import *
from app.img_base64_convert import img_base64_convert as conveter
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.http import QueryDict

def home(request):
    #return render(request, 'index.html')
    return render(request, 'app/app.html')


#get in GUI_TEST.html and get all image we want at images looping
def GUI_test(request):
    data_form = []
    temp = Image_import.objects.all()
    temp = temp.filter(Process_type = '1')
    for data in temp:
        if data.Process_type == '1':
            data_form.append(data.Image.url)
            print(data.Image.url)
    print (data_form)

    if request.method == 'GET':
        Data_form = {}
        Data_form = json.dumps(Data_form)
        return render(request, 'app/GUI_test.html', locals())
    elif request.method == 'POST':
        save_code = request.POST.get('save_code')
        data = diagram.objects.get(Save_code = save_code)
        # Data_form.append({'Save_code': data.Save_code, 'saved_image': data.saved_image})
        Data_form = data.get_all_data()
        #Data_form = json.dumps(Data_form)
        return render(request, 'app/GUI_test.html', locals())

#get in User setting and canvas saving page
def userpage(request):
    Data_form = []
    username = request.user.username
    data = diagram.objects.all()
    #data = list(data)
    print(data)
    for cell in data:
        if cell.username == username:
            Data_form.append({'Save_code': cell.Save_code, 'saved_image': cell.saved_image})
    print(Data_form)
    return render(request, 'app/userpage.html', locals())


#get in Login
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
    if not request.user.is_authenticated:
        print('upload fail')
        dict = {
            'status': 'fail',
            'msg': 'save draw fail',
        }
        return JsonResponse(dict)
        
    if request.method == 'POST':
        if request.POST.get('Json') == '1':
            dict = {'status': 'succes',}
            for key in request.POST:
                print('key: ' + key)
            ############################################
            #getting data
            username = request.user.username
            Save_code = request.POST.get('Save_code')#''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            line = json.loads(request.POST.get('line'))
            circle = json.loads(request.POST.get('circle'))
            rectangle = json.loads(request.POST.get('rectangle'))
            offset = json.loads(request.POST.get('offset'))
            ############################################
            diagram.objects.filter(Save_code = Save_code).update(username = username, line = line,
                 circle = circle, rectangle = rectangle, offset = offset)
            return JsonResponse(dict)
        else:
            print('Type is : ' + request.content_type)
            img = request.FILES.get('img')
            N = 7# lenght of string genarator
            print(img)
            print(request.FILES)
            Save_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
            print(Save_code)
            Json = {
                'Save_code': Save_code,
                }
            temp = diagram(username = request.user.username, Save_code = Save_code, saved_image = img)
            temp.save()
            #diagram.objects.filter(Save_code = 1).update(saved_image = img)
            return JsonResponse(Json)

def product_page(request):
    Data_form = []
    data = product_image.objects.all()
    for cell in data:
        product = product_code.objects.get(product_code = cell.product_code.product_code)
        product = product.product_borad_set.all()[0]
        Data_form.append({
            'product_name': product.product_name,
            'Product_image': cell.Product_image,
        })
    print(Data_form)
    return render(request, 'app/product/product_listup_page.html', locals())

def add_product(request):
    if request.method == 'GET':
        form = add_product_form()
        return render(request, 'app/product/add_product.html', locals())
    elif request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        form = add_product_form(request.POST)
        print(form.is_valid())
        print(request.FILES.get('Product_image'))
        N = 32
        gen_product_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        code = product_code(product_code = gen_product_code)
        code.save()
        code = product_code.objects.get(product_code = gen_product_code)
        product_images_album.objects.get_or_create(product_code = code)
        discuss_borad.objects.get_or_create(product_code = code)
        borad = discuss_borad.objects.get(product_code = code)
        album = product_images_album.objects.get(product_code = code)
        product_image.objects.get_or_create(
            product_code = code,
            Product_image = request.FILES.get('Product_image'),
            main_image = True,
            album = album,
        )
        product_borad.objects.get_or_create(
            product_name = request.POST.get('product_name'),
            Product_delta = request.POST.get('Product_delta'),
            product_code = code,
            Product_image = album,
            User_command = borad,
        )
        return HttpResponseRedirect('GUI_test/') #render(request, 'app/product/product_listup_page.html', locals())