from django.shortcuts import render,redirect
from index.models import Books
from django.db.models import Q
from django import forms
from book_add.views import Truncator
def m(request):
    books=Books.objects.all()
    context={'books':books}
    if request.method=='POST':
        query=request.POST['query']
        search=Books.objects.filter(Q(bid__icontains=query)|Q(btitle__icontains=query)|Q(author__icontains=query)|Q(user__icontains=query))
        context={'books':books,'search':search}
        Truncator()
        return render(request,'mng.html',context)
    Truncator()
    context={'books':books}
    return render(request,'mng.html',context)
# Create your views here.
