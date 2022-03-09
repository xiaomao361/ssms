import imp
from django.shortcuts import render
from django.shortcuts import redirect
import hashlib
from member.models import User


# Create your views here.


# md5
def md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode())     # md5编码
    saltpassword = md5.hexdigest()     # 哈希
    return saltpassword


# 登录验证
def login(request):
    if request.method == "POST":
        body = request.POST
        phone = body['phone']
        password = body['password']
        saltpassword = md5(password)
        user = User.objects.filter(
            phone__exact=phone, password__exact=saltpassword)
        if user:
            request.session['phone'] = phone
            return redirect('/index/')
        else:
            message = "用户验证未通过"
            return render(request, 'login.html', {"message": message})
    else:
        return render(request, 'member/login.html')


# 登出
def logout(request):
    request.session.flush()
    return render(request, 'member/login.html')
