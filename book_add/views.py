from django.shortcuts import render
from index.models import Books

def ba(request):
    books=Books.objects.all()
    context={'books':books}
    bt=None
    au=None
    if request.method=='POST':
        bt=request.POST['btitle']
        au=request.POST['author']
        Truncator()
        add=Books(btitle=bt,author=au)
        add.save()
        add.full_clean()
        return render(request,'book_add.html',context)
    return render(request,'book_add.html',context)

def Truncator():
    for x in Books.objects.all():
        btitle=x.btitle
        if btitle=='':
            truncate=Books.objects.get(bid=x)
            truncate.delete()