from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from art_app.models import Home, Details, Zhangjie, UserProfile

#首页
def index(request):
    nacavit = Home.objects.all()
    datali_list = []
    datalis = Details.objects.filter(home_id=12)
    for datali in datalis:
        datali_list.append(datali)
    return render(request, 'index.html', {'datali_list':datali_list,'nacavit':nacavit})


#导航分类
def details(request):
    book_nav = Home.objects.all()
    class_id = request.GET.get('class_id', '0')
    if class_id == '0':
        detail_list = Details.objects.all()
    else:
        detail_list = Details.objects.filter(home_id = class_id)

    context = {
        'book_detail_list': detail_list,
        'book_nav': book_nav
    }
    return render(request, 'datail_list.html',context=context)


def data_li(request):
    a_id = request.GET.get("details_id",None)
    data_li = Details.objects.filter(details_id=a_id)
    print(data_li)
    return render(request,'datail.html',{'data_li':data_li})





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username and password:
            # 不判断激活状态
            user = authenticate(username=username, password=password)
            if user:
                # 0 表示没有激活  1 表示激活状态  -1   表示用户删除
                if user.is_active:
                    # 记录用户登录状态
                    login(request, user)
                    return redirect('/')
                else:
                    pass
                # 用户没有激活
            else:
                # 用户名密码错误
                pass
        else:
            pass
    return render(request, 'login/login_page.html')


def register(req):
    if req.method == 'GET':
        return render(req, 'login/register_page.html')
    elif req.method == 'POST':
        try:
            username = req.POST.get('username')
            password = req.POST.get('password')
            confirm_password = req.POST.get('confirm_password')
            email = req.POST.get('email')
            if password and username and email and password == confirm_password:
                user = UserProfile.objects.create_user(username=username,
                                                       password=password,
                                                       email=email)
                user.save()
                # 注册成功之后 跳转首页
                return redirect('/')
            else:
                return HttpResponse("注册失败!")
        except Exception  as e:
            return HttpResponse("注册失败")
