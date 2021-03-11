from django.shortcuts import render
from index.models import Books
from datetime import date
from book_add.views import Truncator

def i(request):
    books=Books.objects.filter(status='Available')
    title=None
    issue=Books.objects.filter(btitle=title)
    context={'books':books}
    if request.method=='POST':
        id=request.POST['bid']
        today=date.today()
        username=request.user.username
        issue=Books.objects.filter(bid=id)
        issue.update(status='Issued',user=username,date=today)
    Truncator()
    return render(request,'issue.html',context)