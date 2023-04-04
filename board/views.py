from django.shortcuts import render, redirect
from .models import Board,Reply
from django.core.paginator import Paginator

def dreply(request, bpk, rpk):
    Reply.objects.get(id=rpk).delete()
    return redirect("board:detail", bpk)

def creply(request, bpk):
    b = Board.objects.get(id = bpk)
    r = request.user
    c = request.POST.get('com')
    Reply(board=b, replyer=r, comment=c).save()
    return redirect("board:detail", bpk)

def unlikey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect('board:detail', bpk)

def likey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect('board:detail', bpk)

def index(request):
    pg = request.GET.get('page', 1)
    cate = request.GET.get('cate', "")
    kw = request.GET.get('kw',"")

    if kw:
        if cate == 'sub':
            b = Board.objects.filter(subject__contains=kw)
            # __startswith : 시작하는 단어로 검색
        elif cate == 'wri':
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()
        elif cate == 'con':
            b = Board.objects.filter(content__contains=kw)
    else:
        b = Board.objects.all()

    b = b.order_by("-pubdate") # 정렬 (- : 역방향)
    pag = Paginator(b, 8)
    obj = pag.get_page(pg)
    context = {
        'bs' : obj,
        'kw' : kw,
        'cate' : cate
    }
    return render(request, 'board/index.html', context)

def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        b.delete()
    else:
        pass
    return redirect('board:index')
    

def update(request,bpk):
    b = Board.objects.get(id=bpk)

    if request.user != b.writer:
        return redirect('board:index')
    
    if request.method == 'POST':
        sn = request.POST.get('sub')
        sc = request.POST.get('con')
        b.subject, b.content = sn, sc
        b.save()
        return redirect('board:detail', bpk)    

    context = {
        'b' : b
    }
    return render(request, 'board/update.html', context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {
        'b' : b,
        'rset' : r
    }
    return render(request, 'board/detail.html', context)

def create(request):
    if request.method == "POST":
        sn = request.POST.get('sub')
        sc = request.POST.get('con')
        Board(subject=sn, writer=request.user, content=sc).save()
        return redirect('board:index')
    return render(request, 'board/create.html')