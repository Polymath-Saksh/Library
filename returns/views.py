from django.shortcuts import render
from django.db.models import Q
from index.models import Books
from datetime import date,timedelta
from book_add.views import Truncator
def r(request):
    username=request.user.username
    books=Books.objects.filter(Q(status='Issued')&Q(user=username))
    title=None
    today=date.today()
    for a in books:
        diff=today-a.date
        if diff>timedelta(days=15):
           a.fine=(int(diff.days-15))*2
           a.save()
    context={'books':books}
    if request.method=='POST':
        username=request.user.username
        id=request.POST['bid']
        Books.objects.filter(bid=id).update(user='',date=None,status='Available')
        Truncator()
    return render(request,'returns.html',context)
# Create your views here.
