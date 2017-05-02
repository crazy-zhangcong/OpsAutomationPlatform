from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.forms import Form
from django.forms import widgets
from django.forms import fields

from index import models


import hashlib


# 给密码加密
def str_encrypt(pwd):
    """
    用户输入的密码加密
    :param pwd: 密码
    :return:
    """
    hash = hashlib.md5()
    hash.update(pwd.encode())
    return hash.hexdigest()


# 装饰器 判断是否登录
def is_login(func):
    """判断是否登录"""

    def inner(request, *args, **kwargs):
        username = request.session.get("username")  # 从session中获取用户的username对应的值
        if not username:
            return redirect("/login/")
        return func(request, *args, **kwargs)
    return inner


@is_login
def index_func(request):

    return render(request, 'index/index.html')


# 登录 Form
class loginForm(Form):
    username = fields.CharField(
        error_messages={
            "required": "用户名不能为空！",
        },
        widget=widgets.Input(
            attrs={"class": "form-control", "placeholder": "用户名", "name": "username", "type": "text"})
    )
    password = fields.CharField(
        error_messages={
            "required": "密码不能为空！",
        },
        widget=widgets.PasswordInput(
            attrs={"class": "form-control", "placeholder": "密码", "name": "password", "type": "password"})

    )


def login(request):

    if request.method == "POST":
        obj = loginForm(request.POST)

        if obj.is_valid():
            obj.cleaned_data['password'] = str_encrypt(obj.cleaned_data['password'])
            print(obj.cleaned_data['password'])
            UserProfile_obj = models.UserProfile.objects.filter(**obj.cleaned_data).first()
            if UserProfile_obj:
                request.session['username'] = UserProfile_obj.username
                request.session['user_id'] = UserProfile_obj.id
                request.session['is_login'] = True
                return redirect('/')
            else:  # 用户名和密码不匹配
                obj.errors["password"] = ["用户名或密码错误"]

        return render(request, 'index/login.html', {'obj': obj})
    elif request.method == "GET":
        obj = loginForm()
        return render(request, 'index/login.html', {'obj': obj})


def logout(request):
    request.session.clear()
    return redirect('/login/')