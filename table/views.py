from django.shortcuts import render, redirect
from .models import Table

def delete(request, tpk):
    t = Table.objects.get(id=tpk)
    if request.user == t.작성자:
        t.delete()
    else:
        pass
    return redirect('table:index')

def detail(request, tpk):
    t = Table.objects.get(id=tpk)
    context = {
        't' : t,
    }
    return render(request, 'table/detail.html', context)

def index(request):
    t = Table.objects.all()
    context = {
        'tset' : t
    }
    return render(request, 'table/index.html', context)

def create(request):
    if request.method == "POST":
        주소 = request.POST.get("주소")
        면적 = request.POST.get("면적")
        가격 = request.POST.get("가격")
        종류 = request.POST.get("종류")
        층수 = request.POST.get("층수")
        입주가능일 = request.POST.get("입주가능일")
        방수 = request.POST.get("방수")
        사용승인 = request.POST.get("사용승인")
        난방 = request.POST.get("난방")
        방향 = request.POST.get("방향")
        비고 = request.POST.get("비고")
        주차 = request.POST.get("주차")
        Table(주소=주소, 면적=면적, 가격=가격, 종류=종류, 층수=층수, 입주가능일=입주가능일, 방수=방수, 사용승인=사용승인, 난방=난방, 방향=방향, 비고=비고, 주차=주차,작성자=request.user).save()
        return redirect('table:index')
    return render(request, 'table/create.html')
