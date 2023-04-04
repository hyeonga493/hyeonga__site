from django.shortcuts import render, redirect
from .models import Topic, Choice

def delete(request, tpk):
    tp = Topic.objects.get(id=tpk)
    if tp.maker == request.user:
        tp.delete()
    return redirect('vote:index') 

def cancle(request, tpk):
    u = request.user
    t = Topic.objects.get(id=tpk)
    t.voter.remove(u)
    u.choice_set.get(top=t).choicer.remove(u)
    return redirect('vote:detail', tpk)

def create(request):
    if request.method == 'POST':
        s = request.POST.get('sub')
        c = request.POST.get('scon')
        t = Topic(subject=s, maker=request.user, content=c)
        t.save()
        cn = request.POST.getlist('cname')
        cc = request.POST.getlist('ccom')
        for name, com in zip(cn,cc):
            Choice(top=t, name=name, comment=com).save()
        return redirect('vote:index')
    return render(request, 'vote/create.html')

def vote(request, tpk):
    tp = Topic.objects.get(id=tpk)
    if not request.user in tp.voter.all():
        tp.voter.add(request.user)
        cpk = request.POST.get('cho')
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect('vote:detail', tpk)

def detail(request, tpk):
    tp = Topic.objects.get(id=tpk)
    ch = tp.choice_set.all()
    context = {
        'tp' : tp,
        'ch' : ch,
    }
    return render(request, 'vote/detail.html', context)

def index(request):
    tp = Topic.objects.all()
    context = {
        'tp' : tp,
    }
    return render(request, 'vote/index.html', context)
