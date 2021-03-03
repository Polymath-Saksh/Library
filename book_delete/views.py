from django.shortcuts import render
from index.models import Books
from django.db.models import Q
from book_add.views import Truncator

def bd(request):
    books=Books.objects.all()
    context={'books':books}
    if request.method=='POST':
        id=request.POST['id']
        Books.objects.filter(Q(btitle__icontains=id)|Q(author__icontains=id)).delete()
    Truncator()
    return render(request,'book_delete.html',context)
# Create your views here.
