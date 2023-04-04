from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages

def delete(request):
    u = request.user
    up = request.POST.get('upass')
    if check_password(up, u.password):
        u.pic.delete()
        u.delete()
        return redirect('acc:index')
    else:
        pass
    return redirect('acc:profile')

def chpass(request):
    u = request.user
    cp = request.POST.get('cpass')
    if check_password(cp, u.password):
        np = request.POST.get('npass')
        u.set_password(np)
        u.save()
        return redirect('acc:login')
    return redirect('acc:update')

def update(request):
    if request.method == "POST":
        u = request.user
        um = request.POST.get('umail')
        uc = request.POST.get('ucom')
        up = request.FILES.get('upic')

        u.email, u.comment = um, uc
        if up:
            u.pic.delete()
            u.pic = up
        u.save()
        return redirect('acc:profile')
    return render(request, 'acc/update.html')

def profile(request):
    return render(request, 'acc/profile.html')

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
            messages.success(request, '회원가입 완료. 로그인해주세요.')
            return redirect("acc:login")
        except:
            messages.info(request, '회원가입 실패. 다시 시도해주세요.')
    return render(request, "acc/signup.html")

def ulogout(request):
    logout(request)
    messages.success(request, f'Logout!')
    return redirect('acc:index')

def ulogin(request):

    if request.user.is_authenticated:
        return redirect("acc:index")

    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f'로그인되었습니다.')
            return redirect("acc:index")
        else:
            messages.info(request,f'아이디/비밀번호가 맞지 않습니다.')
    return render(request, "acc/login.html")

def index(request):
    return render(request, 'acc/index.html')