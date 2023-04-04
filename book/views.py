from django.shortcuts import render,redirect
from .models import Book

def create(request):
    if request.method == "POST":
        sn = request.POST.get('sname')
        su = request.POST.get('surl')
        sc = request.POST.get('scon')
        im = bool(request.POST.get('impo'))
        Book(site_name=sn, site_url=su, impo=im, site_con=sc, user=request.user).save()
        return redirect('book:index')
    return render(request, 'book/create.html')

def index(request):
    b = Book.objects.all()
    context = {
        'bset' : b
    }
    return render(request, 'book/index.html', context)
