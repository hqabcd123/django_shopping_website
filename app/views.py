from curses.textpad import rectangle
import random
import string
from time import timezone
from urllib import request, response
from venv import create
from django.shortcuts import render,HttpResponse
from django.http.response import JsonResponse
import os, os.path
import json
from .models import *
from app.img_base64_convert import img_base64_convert as conveter
from django.contrib import auth
from .form import UserCreationForm
from django.http import HttpResponseRedirect
from django.http import QueryDict

adv_list = []

def get_ad_image():
    adv = advertise.objects.all()
    print(adv)
    code = []
    Data = []
    for cell in adv:
        if cell.product_set.code not in code:
            code.append(cell.product_set.code)
            Data.append(cell)
            print(cell.adv_image)

    return Data

def home(request):
    #return render(request, 'index.html')
    return render(request, 'app/app.html')


#get in GUI_TEST.html and get all image we want at images looping
def GUI_test(request):
    adv = get_ad_image()
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
    user = User.objects.get(username=username)
    history = user_history_set.objects.all()
    for cell in history:
        if cell.username == username:
            Data_form.append({
                'history': cell.foodprint_set
            })
    print(Data_form)
    print(user)
    return render(request, 'app/userpage.html', locals())

def userpage_canvas(request):
    Data_form = []
    username = request.user.username
    data = diagram.objects.all()
    #data = list(data)
    print(data)
    for cell in data:
        if cell.username == username:
            Data_form.append({'Save_code': cell.Save_code, 'saved_image': cell.saved_image})
    print(Data_form)
    return render(request, 'app/userpage_canvas.html', locals())


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
        code = product.product_code
        product = product.product_borad_set.all()[0]
        Data_form.append({
            'product_name': product.product_name,
            'Product_image': cell.Product_image,
            'product_code': code,
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
        #create product code object
        #############################################################################################
        code = product_code(product_code = gen_product_code)
        code.save()
        code = product_code.objects.get(product_code = gen_product_code)#get product code object
        #############################################################################################

        product_images_album.objects.get_or_create(product_code = code)#create product image album
        discuss_borad.objects.get_or_create(product_code = code)#create discuss borad
        borad = discuss_borad.objects.get(product_code = code)#save discuss borad to borad
        album = product_images_album.objects.get(product_code = code)#save product image album to album

        product_type.objects.get_or_create(product_type = request.POST.get('product_type'))
        set_of_product_type.objects.get_or_create(
            product_code = code,
            set_of_product_type = product_type.objects.get(product_type = request.POST.get('product_type')),
        )
        product_type_set = set_of_product_type.objects.get(product_code = code)
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
            set_of_product_type = product_type_set,
        )
        return HttpResponseRedirect('GUI_test/') #render(request, 'app/product/product_listup_page.html', locals())


def adv_page(request):
    global adv_list
    context = {
        'adv_list': adv_list,
    }
    if request.method == 'POST':
        data_form = []
        print('POST')
        print(request.POST)
        value = request.POST['value']
        adv = advertise.objects.get(head=value)
        code = adv.product_set.code
        for data in product_set.objects.all():
            if data.code == code:
                print(data.product_code.product_code)
                temp = product_code.objects.get(product_code = data.product_code.product_code)
                print(temp)
                temp1 = temp.product_borad_set.all()[0]
                temp2 = temp.product_image_set.all()[0]
                data_form.append({
                    'product_borad': temp1,
                    'product_image': temp2,
                })
        if len(adv_list) > 0:
            adv_list = []
        adv_list.append({'value': value})
        adv_list.append({'data_form': data_form})
        print(adv_list)
    return render(request, 'app/adv_page.html', context)

def product_delta(request, url_product_code):
    if request.method == 'POST':
        command = request.POST.get('command')
        user = request.user.username
        code = product_code.objects.get(product_code=url_product_code)
        if request.user.is_authenticated:
            discuss_borad.objects.create(
                product_code=code,
                username=user,
                command=command,
            )
            pass
        pass 
    print(url_product_code)
    code = product_code.objects.get(product_code=url_product_code)
    product = code.product_borad_set.all()[0]
    img = code.product_image_set.all()
    board = code.discuss_borad_set.all()
    Data_form = {
        'product_name': product.product_name,
        'product_image': img,
        'product': product,
        'board': board,
    }
    username = request.user.username
    if username:
        history = user_history.objects.create(
            foodprint = product
        )
        history = user_history_set.objects.create(
            foodprint_set = history,
            username = username
        )
    return render(request, 'app/product/product_delta.html', locals())


##