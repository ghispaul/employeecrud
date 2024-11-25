from django.shortcuts import render
from app1.models import emp
# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    if(request.method=="POST"):
        en=request.POST['en']
        a=request.POST['a']
        ad=request.POST['ad']
        e=request.POST['e']

        i=request.FILES['i']

        b=emp.objects.create(ename=en,age=a,address=ad,email=e,image=i)
        b.save()
        return view(request)
    return render(request,'add.html')


def view(request):
    k=emp.objects.all()
    return render(request,'view.html',{'empl':k})


def delete(request,p):
    k=emp.objects.get(id=p)
    k.delete()
    return view(request)

def edit(request,p):
    k=emp.objects.get(id=p)
    if(request.method=="POST"):
        k.ename=request.POST['en']
        k.age=request.POST['a']
        k.address=request.POST['ad']
        k.email=request.POST['e']

        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.image=request.FILES.get('i')

        k.save()
        return view(request)
    return render(request,'edit.html',{'empl':k})

